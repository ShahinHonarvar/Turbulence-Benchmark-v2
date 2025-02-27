def palindromes_between_indices(string):
    letters = []
    for i in range(4, 6):
        if 'a' <= string[i].lower() <= 'z':
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            for k in range(len(letters) - j):
                temp = letters[i:j]
                temp.extend(letters[j + k::-1])
                candidate = ''.join(temp)
                if len(candidate) >= 3:
                    result.add(candidate)
    return result