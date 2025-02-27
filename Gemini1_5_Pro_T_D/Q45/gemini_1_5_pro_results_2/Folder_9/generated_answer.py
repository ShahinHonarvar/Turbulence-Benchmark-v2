def palindromes_between_indices(string):
    letters = []
    for i in range(7):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 7:
        for perm in itertools.permutations(letters):
            candidate = ''.join(perm)
            if candidate == candidate[::-1] and len(candidate) >= 7:
                result.add(candidate)
    return result