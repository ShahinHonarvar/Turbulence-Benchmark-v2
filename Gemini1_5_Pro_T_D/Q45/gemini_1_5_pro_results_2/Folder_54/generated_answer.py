def palindromes_between_indices(string):
    letters = []
    for i in range(4, 10):
        if string[i].isalpha() and string[i].lower() not in letters:
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    word = letters[i] + letters[j] + letters[k] + letters[l]
                    if len(word) >= 4:
                        if word == word[::-1]:
                            palindromes.add(word)
                    if len(word) >= 5:
                        if word[0:len(word) - 1] == word[len(word) - 1:0:-1]:
                            palindromes.add(word)
    return palindromes