def palindromes_between_indices(text):
    letters = []
    for i in range(7):
        if text[i].isalpha():
            letters.append(text[i].lower())
    result = set()
    for s in letters:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters) + 1):
                substring = letters[i:j]
                if len(substring) >= 4:
                    if s == substring[0] and s == substring[-1]:
                        word = ''.join(substring)
                        if word == word[::-1]:
                            result.add(word)
    return result