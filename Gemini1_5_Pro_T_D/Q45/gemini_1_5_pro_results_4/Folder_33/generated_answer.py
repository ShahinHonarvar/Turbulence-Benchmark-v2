def palindromes_between_indices(string):
    letters = []
    for i in range(7, 10):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for permutation in [''.join(p) for p in permutations([letters[i], letters[j], letters[k]])]:
                    if len(permutation) >= 4 and permutation == permutation[::-1]:
                        result.add(permutation)
    return result