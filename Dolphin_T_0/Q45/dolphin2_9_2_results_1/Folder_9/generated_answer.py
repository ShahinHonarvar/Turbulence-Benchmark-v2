import itertools

def palindromes_between_indices(s):
    s = s[:7].lower()
    letters = set(s)
    if len(letters) < 7:
        return set()
    return {lel for lel in letters if lel == lel[::-1]}