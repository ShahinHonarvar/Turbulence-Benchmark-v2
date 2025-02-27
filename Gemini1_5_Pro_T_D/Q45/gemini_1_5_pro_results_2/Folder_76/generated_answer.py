def palindromes_between_indices(string):
    letters = []
    for i in range(1, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            for permutation in itertools.permutations(letters[i:j]):
                candidate = ''.join(permutation)
                if len(candidate) >= 4 and candidate == candidate[::-1]:
                    result.add(candidate)
    return result