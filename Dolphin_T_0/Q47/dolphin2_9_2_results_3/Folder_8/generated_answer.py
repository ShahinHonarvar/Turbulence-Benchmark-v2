def palindromes_of_specific_lengths(s):
    s = ''.join((c for c in s if c.isalpha()))
    return set((s[i:j] for i in range(len(s) - 49) for j in range(i + 50, min(i + 52, len(s) + 1))))