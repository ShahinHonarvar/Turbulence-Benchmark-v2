def palindromes_between_indices(string):
    letters = []
    for i in range(1, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for perm in itertools.permutations(letters):
        candidate = ''.join(perm)
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            result.add(candidate)
    return result