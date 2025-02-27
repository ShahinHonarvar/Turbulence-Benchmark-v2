def palindromes_between_indices(s):
    letters = sorted([c.lower() for c in s[3:9] if c.isalpha()])
    results = set()
    for perm in itertools.permutations(letters):
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            results.add(word)
    return results