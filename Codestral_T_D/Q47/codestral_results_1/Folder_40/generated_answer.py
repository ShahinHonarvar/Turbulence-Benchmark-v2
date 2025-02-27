def palindromes_of_specific_lengths(s):
    s = s[:6]
    s = ''.join((c for c in s if c.isalpha()))
    s = s.lower()
    return {s[i:j] for i in range(len(s)) for j in range(i + 3, i + 6) if s[i:j] == s[i:j][::-1]}