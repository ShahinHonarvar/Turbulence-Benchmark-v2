def palindromes_between_indices(string):
    letters = []
    for i in range(1, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for s in set([''.join(p) for p in itertools.permutations(letters)]):
        if len(s) >= 6 and s == s[::-1]:
            result.add(s)
    return result