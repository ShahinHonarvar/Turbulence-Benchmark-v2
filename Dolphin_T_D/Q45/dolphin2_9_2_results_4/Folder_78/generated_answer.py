def palindromes_between_indices(s):
    letters = s[5:9].lower()
    chars = set(letters)
    if len(chars) < 2:
        return set()
    return {w for w in set(map(''.join, itertools.permutations(letters))) if w == w[::-1]}