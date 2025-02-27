def palindromes_between_indices(string):
    letters = []
    for i in range(3, 10):
        if i < len(string) and string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for s in range(3, len(letters) + 1):
        for i in range(len(letters) - s + 1):
            substring = letters[i:i + s]
            if substring == substring[::-1]:
                result.add(''.join(substring))
    return result