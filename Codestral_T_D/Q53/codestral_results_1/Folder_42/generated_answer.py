def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = len(s)
    for length in range(4, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes