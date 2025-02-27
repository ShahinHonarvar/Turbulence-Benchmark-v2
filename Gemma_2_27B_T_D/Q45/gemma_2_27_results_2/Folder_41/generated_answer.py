def palindromes_between_indices(text):
    letters = text[2:4].lower()
    result = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            substring = letters[i:j + 1]
            if substring == substring[::-1] and len(substring) >= 3:
                result.add(substring)
    return result