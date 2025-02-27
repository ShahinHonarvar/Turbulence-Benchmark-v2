def palindromes_between_indices(string):
    letters = []
    for i in range(6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(''.join(substring))
    return result