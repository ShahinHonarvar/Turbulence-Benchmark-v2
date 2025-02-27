def palindromes_between_indices(s):
    letters = set([c.lower() for c in s[:8] if c.isalpha()])
    length = len(letters)
    palindromes = set()
    for _ in range(length, 0, -1):
        for subset in combinations(letters, _):
            if len(subset) < 4:
                break
            word = ''.join(sorted(list(subset)))
            if word == word[::-1] and _ >= 4:
                palindromes.add(word.lower())
    return palindromes