def palindrome_of_length_n(s):
    i = 0
    palindromes = set()
    while i < len(s) - 6:
        j = i + 7
        while j <= len(s):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
            j += 1
        i += 1
    return palindromes