def palindromes_between_indices(text):
    letters = text[1:5]
    palindromes = set()
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            for k in range(j + 1, len(letters)):
                word = letters[i].lower() + letters[j].lower() + letters[k].lower() + letters[k].lower() + letters[j].lower() + letters[i].lower()
                if word == word[::-1] and len(word) >= 3:
                    palindromes.add(word)
    return palindromes