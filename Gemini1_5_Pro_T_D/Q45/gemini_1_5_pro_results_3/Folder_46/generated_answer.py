def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:10] if c.isalpha())).lower()
    result = set()
    if len(letters) < 6:
        return result
    for i in range(len(letters) - 5):
        for j in range(i + 5, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result