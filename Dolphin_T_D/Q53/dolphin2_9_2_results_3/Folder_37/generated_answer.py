def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 67
    palindromes = set()
    for length in range(n, len(s) + 1):
        for start in range(0, len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes