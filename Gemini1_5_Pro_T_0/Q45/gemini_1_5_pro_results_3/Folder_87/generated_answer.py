def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:10] if c.isalpha())).lower()
    result = set()
    if len(letters) < 3:
        return result
    for i in range(len(letters) - 2):
        for j in range(i + 2, len(letters) + 1):
            substring = letters[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result