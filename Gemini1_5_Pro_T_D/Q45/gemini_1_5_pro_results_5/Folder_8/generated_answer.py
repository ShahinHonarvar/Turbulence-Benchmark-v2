def palindromes_between_indices(string):
    letters = []
    for i in range(1, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    for m in range(l + 1, len(letters)):
                        word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if len(word) >= 5:
                            if word == word[::-1]:
                                result.add(word)
    return result