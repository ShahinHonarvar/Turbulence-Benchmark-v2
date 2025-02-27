def palindromes_between_indices(string):
    letters = []
    for i in range(0, 3):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) < 3:
        return result
    for i in range(0, len(letters)):
        for j in range(0, len(letters)):
            for k in range(0, len(letters)):
                temp = letters[i] + letters[j] + letters[k]
                if len(temp) >= 3:
                    if temp == temp[::-1]:
                        result.add(temp)
    return result