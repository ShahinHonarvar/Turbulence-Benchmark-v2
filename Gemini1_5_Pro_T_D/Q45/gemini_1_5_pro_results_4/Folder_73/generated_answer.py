def palindromes_between_indices(string):
    letters = []
    for i in range(3, 7):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for permutation in [letters[i] + letters[j] + letters[k], letters[i] + letters[k] + letters[j], letters[j] + letters[i] + letters[k], letters[j] + letters[k] + letters[i], letters[k] + letters[i] + letters[j], letters[k] + letters[j] + letters[i]]:
                    if permutation == permutation[::-1]:
                        palindromes.add(permutation)
    return palindromes