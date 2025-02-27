def palindromes_between_indices(s):
    s = s[7:9].lower()
    return set((a + b + a for a in s for b in s if a != b and a + b + a in s)) or set()