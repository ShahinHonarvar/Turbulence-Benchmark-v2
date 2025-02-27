def palindromes_between_indices(string):
    letters = ''.join(sorted((c for c in string[2:4] if c.isalpha()))).lower()
    result = set()
    if len(letters) < 3:
        return result
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters) + 1):
                substring = letters[i:k]
                if substring == substring[::-1]:
                    result.add(substring)
    return result