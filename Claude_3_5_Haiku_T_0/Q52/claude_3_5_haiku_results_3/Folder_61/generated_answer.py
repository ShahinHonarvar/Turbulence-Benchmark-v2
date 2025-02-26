def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 73):
        for j in range(i + 74, n + 1):
            substring = s[i:j]
            if len(substring) == 74 and substring.isalpha() and (substring == substring[::-1]):
                palindromes.add(substring)
    return palindromes