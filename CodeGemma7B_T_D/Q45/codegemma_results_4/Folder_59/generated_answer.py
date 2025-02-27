def palindromes_between_indices(text):
    valid_chars = set('abcdefghijklmnopqrstuvwxyz')
    result = set()
    for i in range(len(text) - 3):
        for j in range(i + 2, len(text)):
            substring = text[i:j + 1]
            if all((char in valid_chars for char in substring)):
                if substring == substring[::-1]:
                    result.add(substring.upper())
    return result