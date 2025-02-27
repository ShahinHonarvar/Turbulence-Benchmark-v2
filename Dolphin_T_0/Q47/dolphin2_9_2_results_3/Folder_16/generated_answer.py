def palindromes_of_specific_lengths(s):
    s = s[15:87]
    return set((p for p in (s[i:j] for i in range(len(s)) for j in range(i + 51, min(len(s), i + 61))) if p.lower() == p.lower()[::-1]))