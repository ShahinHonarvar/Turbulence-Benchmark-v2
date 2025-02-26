def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 138, n + 1):
            substr = s[i:j]
            if substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes