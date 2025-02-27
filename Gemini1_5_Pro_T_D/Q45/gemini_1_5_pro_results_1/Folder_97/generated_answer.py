def palindromes_between_indices(string):
    letters = []
    for i in range(5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters) - 1):
            for k in range(j + 1, len(letters)):
                substring = letters[i] + letters[j] + letters[k]
                if substring == substring[::-1]:
                    result.add(substring)
    return result