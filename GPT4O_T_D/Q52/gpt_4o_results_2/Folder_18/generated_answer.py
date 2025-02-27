def palindrome_of_length_n(s):
    n = 392
    palindromes = set()
    if len(s) < n:
        return palindromes
    s = ''.join([c.lower() for c in s if c.isalpha()])
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes