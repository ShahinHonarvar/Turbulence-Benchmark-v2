def palindromes_between_indices(text):
    letters = text[4:7]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(3):
                    word = ''.join([letters[i], letters[j], letters[k]])
                    if word.lower() == word[::-1].lower() and len(word) >= 3:
                        palindromes.add(word)
    return palindromes