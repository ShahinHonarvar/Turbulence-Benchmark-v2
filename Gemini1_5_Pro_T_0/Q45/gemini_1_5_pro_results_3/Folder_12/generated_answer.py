def palindromes_between_indices(text):
    letters = ''.join((c for c in text[3:9] if c.isalpha())).lower()
    result = set()
    if len(letters) >= 4:
        for i in range(len(letters) - 3):
            for j in range(i + 3, len(letters) + 1):
                substring = letters[i:j]
                if substring == substring[::-1]:
                    result.add(substring)
    return result