def palindromes_between_indices(string):
    letters = []
    for i in range(2, 5):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    substring = letters[i] + letters[j] + letters[k]
                    if substring == substring[::-1]:
                        result.add(substring)
                    substring = letters[i] + letters[k] + letters[j]
                    if substring == substring[::-1]:
                        result.add(substring)
                    substring = letters[j] + letters[i] + letters[k]
                    if substring == substring[::-1]:
                        result.add(substring)
                    substring = letters[j] + letters[k] + letters[i]
                    if substring == substring[::-1]:
                        result.add(substring)
                    substring = letters[k] + letters[i] + letters[j]
                    if substring == substring[::-1]:
                        result.add(substring)
                    substring = letters[k] + letters[j] + letters[i]
                    if substring == substring[::-1]:
                        result.add(substring)
    return result