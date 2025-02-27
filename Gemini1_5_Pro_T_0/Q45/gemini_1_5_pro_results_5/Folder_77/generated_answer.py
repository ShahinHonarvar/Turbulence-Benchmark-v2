def palindromes_between_indices(string):
    letters = []
    for i in range(4, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    if len(letters) >= 4:
        for i in range(len(letters) - 3):
            for j in range(i + 3, len(letters) + 1):
                substring = letters[i:j]
                if len(substring) >= 4:
                    if substring == substring[::-1]:
                        result.add(''.join(substring))
    return result