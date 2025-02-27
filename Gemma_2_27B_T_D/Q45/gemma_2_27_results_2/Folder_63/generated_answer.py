def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[:4])).lower()
    if len(letters) < 3:
        return set()
    return {p for p in {''.join(sorted(p)) for p in itertools.permutations(letters)} if p == p[::-1] and len(p) >= 3}