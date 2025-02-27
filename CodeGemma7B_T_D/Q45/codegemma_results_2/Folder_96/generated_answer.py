def palindromes_between_indices(text):
    text = text.lower()
    result = set()
    for i in range(len(text) - 5):
        for j in range(i + 6, len(text) + 1):
            substring = text[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result