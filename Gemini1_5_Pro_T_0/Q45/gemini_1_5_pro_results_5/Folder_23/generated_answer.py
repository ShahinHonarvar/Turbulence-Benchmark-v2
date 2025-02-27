def palindromes_between_indices(string):
    letters = []
    for i in range(0, 7):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            current = letters[i:j]
            for k in range(len(current) // 2):
                if current[k] != current[len(current) - k - 1]:
                    break
            else:
                if len(current) >= 4:
                    result.add(''.join(current))
    return result