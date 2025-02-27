def palindromes_between_indices(s):
    letters = set([ch.lower() for ch in s[4:9] if ch.isalpha()])
    result = set()
    if len(letters) < 3:
        return result
    for length in range(3, len(letters) + 1):
        for subset in combinations(letters, length):
            for word in [''.join(p) for p in permutations(subset)]:
                if word == word[::-1]:
                    result.add(word)
    return result