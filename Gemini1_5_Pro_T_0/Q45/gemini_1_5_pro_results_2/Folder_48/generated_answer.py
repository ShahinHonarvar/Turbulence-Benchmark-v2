def palindromes_between_indices(string):
    letters = []
    for i in range(6, 9):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    palindromes = set()
    if len(letters) > 3:
        for i in range(len(letters)):
            for j in range(i + 1, len(letters)):
                for k in range(j + 1, len(letters)):
                    for l in range(k + 1, len(letters)):
                        substring = letters[i] + letters[j] + letters[k] + letters[l]
                        if substring == substring[::-1]:
                            palindromes.add(substring)
    return palindromes