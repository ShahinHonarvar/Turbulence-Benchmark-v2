def palindromes_between_indices(s):
    letters = ''
    for i in range(6, 10):
        if s[i].isalpha():
            letters += s[i].lower()
    result = set()
    n = len(letters)
    for i in range(5, n + 1):
        for subset in combinations(letters, i):
            for p in permutations(subset):
                word = ''.join(p)
                if word == word[::-1]:
                    result.add(word.lower())
    return result