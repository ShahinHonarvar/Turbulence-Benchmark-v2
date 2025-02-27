def palindromes_between_indices(string):
    letters = []
    for i in range(4, 9):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                temp = letters[i] + letters[j] + letters[k]
                if temp == temp[::-1]:
                    result.add(temp)
    return result