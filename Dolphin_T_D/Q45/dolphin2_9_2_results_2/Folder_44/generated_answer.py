def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:8]]
    return set((c for c in letters if letters.count(c) > 1 and len(c) >= 3))