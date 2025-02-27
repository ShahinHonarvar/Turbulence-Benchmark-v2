def palindromes_of_specific_lengths(s):
    s = s[17:88]
    s = ''.join((c for c in s if c.isalpha()))
    palindromes = {c.lower() for i in range(len(s)) for j in range(i + 2, len(s) + 1) if s[i:j].lower() == s[i:j].lower()[::-1] and 38 <= j - i <= 60}
    return palindromes