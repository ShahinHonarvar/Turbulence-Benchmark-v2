def palindromes_between_indices(s):
    letters = set(s[4:8].lower())
    if not all((c in 'abcdefghijklmnopqrstuvwxyz' for c in letters)):
        return set()
    return {w for w in (''.join(p) for i in range(5, 9) for p in permutations(s[i - 5:i], i - 5)) if w.lower() == w[::-1]}