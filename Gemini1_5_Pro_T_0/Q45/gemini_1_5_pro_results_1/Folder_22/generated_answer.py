def palindromes_between_indices(string):
    letters = []
    for i in range(5, 7):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    temp = letters[i] + letters[j] + letters[k]
                    if temp == temp[::-1]:
                        result.add(temp)
                    temp = letters[i] + letters[k] + letters[j]
                    if temp == temp[::-1]:
                        result.add(temp)
                    temp = letters[j] + letters[i] + letters[k]
                    if temp == temp[::-1]:
                        result.add(temp)
                    temp = letters[j] + letters[k] + letters[i]
                    if temp == temp[::-1]:
                        result.add(temp)
                    temp = letters[k] + letters[i] + letters[j]
                    if temp == temp[::-1]:
                        result.add(temp)
                    temp = letters[k] + letters[j] + letters[i]
                    if temp == temp[::-1]:
                        result.add(temp)
    return result