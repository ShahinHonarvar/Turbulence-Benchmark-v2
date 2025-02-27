def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 77):
        for j in range(i + 78, len(s) + 1):
            substring = s[i:j]
            if substring.isalpha() and substring == substring[::-1] and (len(substring) == 78):
                palindromes.add(substring)
    return palindromes