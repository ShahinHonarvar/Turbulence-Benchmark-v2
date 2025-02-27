def palindrome_of_length_at_least_n(s):
    s_low = s.lower()
    palindromes = set()
    for length in range(119, len(s) + 1):
        for start in range(len(s) - length + 1):
            substring = s_low[start:start + length]
            if substring == substring[::-1]:
                palindromes.add(''.join((c for c in substring if c.isalpha())))
    return palindromes