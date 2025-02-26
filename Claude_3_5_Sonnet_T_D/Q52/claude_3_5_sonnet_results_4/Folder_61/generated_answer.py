def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    n = len(s)
    palindromes = set()
    for i in range(n - 73):
        substr = s[i:i + 74]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes