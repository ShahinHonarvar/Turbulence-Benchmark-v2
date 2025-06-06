def palindromes_between_indices(text):
    letters = text[1:5].lower()
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    word = letters[i] + letters[j] + letters[k] + letters[l]
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes