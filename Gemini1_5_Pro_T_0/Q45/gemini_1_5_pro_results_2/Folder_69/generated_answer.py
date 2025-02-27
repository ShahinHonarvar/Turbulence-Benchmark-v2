def palindromes_between_indices(string):
    letters = []
    for i in range(4):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) < 4:
        return result
    for i in range(len(letters)):
        for j in range(len(letters)):
            if i != j:
                for k in range(len(letters)):
                    if i != k and j != k:
                        for l in range(len(letters)):
                            if i != l and j != l and (k != l):
                                word = letters[i] + letters[j] + letters[k] + letters[l]
                                if word == word[::-1]:
                                    result.add(word)
    return result