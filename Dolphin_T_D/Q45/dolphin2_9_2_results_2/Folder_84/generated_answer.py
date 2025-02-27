def palindromes_between_indices(s):
    sub = ''.join(sorted([c for c in s[4:10] if c.isalpha()]))
    palindromes = set()
    for size in range(3, len(sub) + 1):
        combinations = itertools.permutations(sub, size)
        for combo in combinations:
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes