def palindromes_between_indices(string):
    letters = []
    for i in range(7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters) - 1):
            for k in range(j + 1, len(letters)):
                temp = [letters[i], letters[j], letters[k]]
                if temp == temp[::-1]:
                    result.add(''.join(temp))
    return result