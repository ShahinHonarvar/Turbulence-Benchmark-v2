def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:5] if c.isalpha()]
    shuffled_letters = set((''.join(p) for p in permutations(letters, len(letters))))
    palindromes = set((w for w in shuffled_letters if w == w[::-1] and len(w) >= 3))
    return palindromes