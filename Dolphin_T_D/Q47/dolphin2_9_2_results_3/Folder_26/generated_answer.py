def palindromes_of_specific_lengths(s):
    s = s[23:][:60]
    return set((p for size in range(21, 32) for p in set((s[i:i + size] for i in range(len(s) - size + 1))) if p.lower() == p.lower()[::-1] and p.islower()))