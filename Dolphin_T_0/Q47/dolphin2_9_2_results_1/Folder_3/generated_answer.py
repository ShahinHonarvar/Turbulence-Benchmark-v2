def palindromes_of_specific_lengths(s):
    s = ''.join((c.lower() for c in s[27:96] if c.isalpha()))
    return set((s[i:j] for i in range(len(s)) for j in range(i + 49, min(i + 52, len(s))) if s[i:j] == s[i:j][::-1]))