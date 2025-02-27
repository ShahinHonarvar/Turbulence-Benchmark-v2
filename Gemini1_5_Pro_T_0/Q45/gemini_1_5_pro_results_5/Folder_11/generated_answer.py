def palindromes_between_indices(string):
    letters = []
    for i in range(3, 8):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) - 3):
        for j in range(i + 1, len(letters) - 2):
            for k in range(j + 1, len(letters)):
                for l in range(i, len(letters)):
                    temp = letters[i] + letters[j] + letters[k] + letters[l]
                    if temp == temp[::-1]:
                        result.add(temp)
    return result