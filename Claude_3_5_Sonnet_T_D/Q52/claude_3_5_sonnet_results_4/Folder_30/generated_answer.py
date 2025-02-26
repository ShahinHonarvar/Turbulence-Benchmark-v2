def palindrome_of_length_n(s):
    s = ''.join((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(len(s) - 93):
        substr = s[i:i + 94]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes