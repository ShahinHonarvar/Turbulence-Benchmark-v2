def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for i in range(n - 66):
        for j in range(i + 67, n + 1):
            substr = s[i:j]
            if len(substr) == 67 and substr.isalpha() and (substr == substr[::-1]):
                palindromes.add(substr)
    return palindromes