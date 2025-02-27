def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 51, len(s) + 1):
            substring = s[i:j].lower()
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes