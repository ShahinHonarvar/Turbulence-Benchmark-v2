def palindromes_between_indices(string):
    letters = []
    for i in range(5, 10):
        if 97 <= ord(string[i].lower()) <= 122:
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            for k in range(j, len(letters)):
                for l in range(k, len(letters)):
                    for m in range(l, len(letters)):
                        word = letters[i] + letters[j] + letters[k] + letters[l] + letters[m]
                        if len(word) >= 5 and word == word[::-1]:
                            palindromes.add(word)
    return palindromes