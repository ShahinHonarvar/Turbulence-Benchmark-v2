def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    n = len(s)
    for i in range(n - 6):
        substr = s[i:i + 7]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes