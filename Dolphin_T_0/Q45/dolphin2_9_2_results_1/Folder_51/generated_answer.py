def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6]]
    return set((''.join(p) for i in range(len(letters)) for p in permutations(letters, i + 3) if p == p[::-1]))