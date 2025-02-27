def palindromes_between_indices(text):
    letters = text[7:10]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                for l in range(k + 1, len(letters)):
                    word = letters[i] + letters[j] + letters[k] + letters[l]
                    if word.lower() == word[::-1].lower() and len(word) >= 4:
                        palindromes.add(word)
    return palindromes