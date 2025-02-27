def palindromes_between_indices(s):
    letters = ''
    for i in range(1, 10):
        letters += s[i].lower()
    letters = set(letters)
    if len(letters) < 7:
        return set()
    palindromes = set()
    for p in range(7, len(letters) + 1):
        for w in combinations(letters, p):
            for i in permutations(w):
                if i == i[::-1] and len(i) >= 7:
                    palindromes.add(''.join(i))
    return palindromes