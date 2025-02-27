def palindromes_between_indices(string):
    letters = []
    for i in range(2, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    if len(letters) >= 4:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    for l in range(k + 1, len(letters)):
                        for permutation in [''.join(p) for p in permutations([letters[i], letters[j], letters[k], letters[l]])]:
                            if len(permutation) >= 4 and permutation == permutation[::-1]:
                                palindromes.add(permutation)
    return palindromes