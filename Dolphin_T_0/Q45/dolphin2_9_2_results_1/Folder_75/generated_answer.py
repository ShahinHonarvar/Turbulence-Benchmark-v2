def palindromes_between_indices(s):
    letters = s[2:5].lower()
    return set((''.join(x) for x in itertools.permutations(letters) if x == x[::-1] and len(x) >= 3))