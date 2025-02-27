def palindromes_between_indices(text):
    letters = text[1:4].lower()
    return set((p for p in {''.join(perm) for perm in permutations(letters)} if len(p) >= 4 and p == p[::-1]))