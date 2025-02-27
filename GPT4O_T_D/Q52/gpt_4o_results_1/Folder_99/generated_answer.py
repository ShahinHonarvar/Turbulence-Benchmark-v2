def palindrome_of_length_n(s):
    n = 420
    s = ''.join((c for c in s if c.isalpha())).lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if substr == substr[::-1]:
            palindromes.add(substr)
    return palindromes