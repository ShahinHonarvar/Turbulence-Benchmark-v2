def palindromes_between_indices(string):
    letters = []
    for i in range(4, 8):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for permutation in [''.join(p) for p in permutations([letters[i], letters[j], letters[k], letters[l]])]:
                        if len(permutation) >= 4 and permutation == permutation[::-1]:
                            result.add(permutation)
    return result