def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 27):
        for j in range(i + 28, n + 1):
            substring = s[i:j]
            if len(substring) == 28 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes