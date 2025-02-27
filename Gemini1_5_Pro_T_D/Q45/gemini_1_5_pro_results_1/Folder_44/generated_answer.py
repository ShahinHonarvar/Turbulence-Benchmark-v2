def palindromes_between_indices(string):
    letters = []
    for i in range(2, 8):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 3 and substring == substring[::-1]:
                result.add(''.join(substring))
    return result