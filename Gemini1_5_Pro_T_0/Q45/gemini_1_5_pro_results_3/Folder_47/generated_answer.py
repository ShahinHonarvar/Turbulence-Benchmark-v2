def palindromes_between_indices(string):
    s = string[3:8].lower()
    letters = []
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            letters.append(char)
    result = set()
    if len(letters) < 5:
        return result
    for i in range(len(letters) - 4):
        for j in range(i + 1, len(letters) - 3):
            for k in range(j + 1, len(letters) - 2):
                for l in range(k + 1, len(letters) - 1):
                    for m in range(l + 1, len(letters)):
                        temp = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if temp == temp[::-1]:
                            result.add(temp)
    return result