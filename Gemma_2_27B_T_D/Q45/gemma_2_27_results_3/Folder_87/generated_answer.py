def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:10])).lower()
    return {word for word in set((w for w in (''.join(p) for p in permutations(letters)) if len(w) >= 3 and w == w[::-1]))}