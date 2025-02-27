def palindromes_between_indices(string):
    letters = []
    for i in range(4, 8):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    palindromes = set()
    if len(letters) >= 4:
        for i in range(len(letters) - 3):
            for j in range(i + 1, len(letters) - 2):
                for k in range(j + 1, len(letters) - 1):
                    for l in range(k + 1, len(letters)):
                        word = letters[i] + letters[j] + letters[k] + letters[l]
                        if word == word[::-1]:
                            palindromes.add(word)
    return palindromes