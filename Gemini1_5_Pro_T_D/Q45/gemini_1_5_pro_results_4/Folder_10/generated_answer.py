def palindromes_between_indices(string):
    letters = []
    for i in range(0, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for s in letters:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                temp = letters[i:j + 1]
                temp.insert(0, s)
                if len(temp) >= 3:
                    if temp == temp[::-1]:
                        result.add(''.join(temp).lower())
    return result