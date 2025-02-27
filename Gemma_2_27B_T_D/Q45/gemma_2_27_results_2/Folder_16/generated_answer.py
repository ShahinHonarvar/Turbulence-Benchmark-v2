def palindromes_between_indices(text):
    letters = text[6:10].lower()
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    for letter5 in letters:
                        if letter1 == letter5 and letter2 == letter4:
                            palindromes.add(letter1 + letter2 + letter3 + letter4 + letter5)
    return palindromes