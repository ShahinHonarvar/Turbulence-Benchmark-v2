def palindromes_between_indices(string):
    letters = []
    for i in range(6, 9):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    if len(letters) > 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    temp = letters[i] + letters[j] + letters[k]
                    if temp[::-1] in result:
                        result.add(temp)
                    else:
                        result.add(temp[::-1])
    return result