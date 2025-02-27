def palindromes_between_indices(string):
    letters = []
    for i in range(5, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    word = letters[i] + letters[j] + letters[k]
                    if word == word[::-1]:
                        result.add(word)
    return result