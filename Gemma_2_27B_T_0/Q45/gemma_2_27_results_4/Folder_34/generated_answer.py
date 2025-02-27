def palindromes_between_indices(text):
    letters = text[5:8]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    word = letter1 + letter2 + letter3 + letter4
                    if word.lower() == word[::-1].lower() and len(word) >= 4:
                        palindromes.add(word)
    return palindromes