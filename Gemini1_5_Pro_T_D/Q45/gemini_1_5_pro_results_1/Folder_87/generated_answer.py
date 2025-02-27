def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:10] if c.isalpha())).lower()
    result = set()
    if len(letters) < 3:
        return result
    for i in range(0, len(letters) - 2):
        for j in range(i + 1, len(letters) - 1):
            for k in range(j + 1, len(letters)):
                substring = letters[i] + letters[j] + letters[k]
                if substring == substring[::-1]:
                    result.add(substring)
    return result