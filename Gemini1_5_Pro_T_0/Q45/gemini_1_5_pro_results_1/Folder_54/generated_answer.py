def palindromes_between_indices(string):
    letters = []
    for i in range(4, 10):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters)):
        for j in range(i + 3, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 4:
                if substring == substring[::-1]:
                    result.add(''.join(substring))
    return result