def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    palindromes = set()
    for length in range(3, n + 1):
        for start in range(n - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes