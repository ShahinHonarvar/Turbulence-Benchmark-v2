def palindromes_between_indices(s):
    chars = [c.lower() for c in s[:7] if c.isalpha() and c.isascii()]
    if len(set(chars)) < 7:
        return set()
    permutations = [''.join(p) for p in permutations(chars)]
    palindromes = [p for p in permutations if p == p[::-1]]
    return set(palindromes)