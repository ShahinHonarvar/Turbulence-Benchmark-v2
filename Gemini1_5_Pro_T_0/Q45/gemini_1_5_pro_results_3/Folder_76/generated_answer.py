def palindromes_between_indices(text):
    letters = []
    for i in range(1, 5):
        if text[i:i + 1].isalpha() and len(text[i:i + 1]) > 0:
            letters.append(text[i:i + 1].lower())
    result = set()
    for i in range(len(letters) + 1):
        for j in range(i + 1, len(letters) + 1):
            current = letters[i:j]
            for k in range(len(current) // 2):
                if current[k] != current[len(current) - 1 - k]:
                    break
            else:
                if len(current) >= 4:
                    result.add(''.join(current))
    return result