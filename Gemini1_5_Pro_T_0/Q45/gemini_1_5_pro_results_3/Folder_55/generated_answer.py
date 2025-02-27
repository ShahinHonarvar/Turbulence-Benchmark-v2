def palindromes_between_indices(string):
    letters = []
    for i in range(0, 3):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) < 3:
        return result
    for i in range(len(letters)):
        for j in range(len(letters)):
            for k in range(len(letters)):
                if i != j and i != k and (j != k):
                    temp = letters[i] + letters[j] + letters[k]
                    if temp == temp[::-1]:
                        result.add(temp)
    return result