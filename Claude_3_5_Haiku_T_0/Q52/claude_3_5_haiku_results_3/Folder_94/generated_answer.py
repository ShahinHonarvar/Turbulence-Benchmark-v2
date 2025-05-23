def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 92):
        for j in range(i + 93, n + 1):
            substring = s[i:j]
            if len(substring) == 93 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes