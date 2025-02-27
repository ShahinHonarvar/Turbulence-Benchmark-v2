def palindromes_between_indices(string):
    letters = set()
    for i in range(8):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    word = letter1 + letter2 + letter3 + letter4
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes