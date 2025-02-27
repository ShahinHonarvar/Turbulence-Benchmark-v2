def palindromes_of_specific_lengths(s):
    s = s[100:301]
    s = ''.join((c.lower() for c in s if c.isalpha()))
    return {s[i:j + 1] for i in range(len(s)) for j in range(i + 49, min(i + 100, len(s))) if s[i:j + 1] == s[i:j + 1][::-1]}