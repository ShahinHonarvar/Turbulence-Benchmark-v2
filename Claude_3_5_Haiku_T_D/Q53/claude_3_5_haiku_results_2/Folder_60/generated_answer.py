def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for length in range(80, n + 1):
        for start in range(n - length + 1):
            substr = s[start:start + length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes