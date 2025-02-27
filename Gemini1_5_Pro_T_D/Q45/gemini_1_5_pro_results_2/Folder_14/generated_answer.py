def palindromes_between_indices(string):
    letters = []
    for i in range(4, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters) - 2):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                word = letters[i] + letters[j] + letters[k]
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes