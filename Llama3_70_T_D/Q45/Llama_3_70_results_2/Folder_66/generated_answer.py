def palindromes_between_indices(s):
    s = s[:6].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for i in range(5, 1 + len(letters)):
        for p in itertools.combinations(letters, i):
            for q in itertools.permutations(p):
                w = ''.join(q)
                if w == w[::-1]:
                    palindromes.add(w)
    return palindromes