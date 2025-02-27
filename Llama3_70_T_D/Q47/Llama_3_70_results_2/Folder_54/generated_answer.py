def palindromes_of_specific_lengths(s):
    s = s[27:78].lower()
    return set((c for i in range(len(s)) for c in [s[i:i + j] for j in range(18, 20)] if c == c[::-1] and c.isalpha()))