def palindromes_between_indices(s):
    letters = []
    for i in range(4, 9):
        if s[i].isalpha():
            letters.append(s[i].lower())
    if len(set(letters)) < 5:
        return set()
    palindromes = set()
    for p in range(5, len(letters) + 1):
        for comb in combinations(letters, p):
            if comb == comb[::-1]:
                palindromes.add(''.join(comb))
    return palindromes