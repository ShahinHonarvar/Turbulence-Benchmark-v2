def palindromes_between_indices(string):
    letters = []
    for i in range(4):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    temp = [letters[i], letters[j], letters[k]]
                    for permutation in itertools.permutations(temp):
                        word = ''.join(permutation)
                        if word == word[::-1]:
                            result.add(word)
    return result