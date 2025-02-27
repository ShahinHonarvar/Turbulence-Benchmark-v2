def palindromes_between_indices(string):
    letters = []
    for i in range(3, 8):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters) + 1):
            substring = letters[i:j]
            if len(substring) >= 6:
                for k in range(len(substring) // 2 + 1):
                    if substring[:k] == substring[k:][::-1]:
                        palindromes.add(''.join(substring))
    return palindromes