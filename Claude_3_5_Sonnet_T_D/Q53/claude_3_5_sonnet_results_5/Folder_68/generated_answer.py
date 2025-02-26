def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s.lower()))
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 20, n):
            substr = s[i:j + 1]
            if substr == substr[::-1] and len(substr) >= 21:
                palindromes.add(substr)
    return palindromes