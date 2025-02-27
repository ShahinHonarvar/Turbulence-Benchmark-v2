def palindromes_between_indices(string):
    letters = []
    for i in range(3, 7):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                temp = [letters[i], letters[j], letters[k]]
                for permutation in [''.join(p) for p in permutations(temp)]:
                    if len(permutation) >= 3 and permutation == permutation[::-1]:
                        result.add(permutation)
    return result