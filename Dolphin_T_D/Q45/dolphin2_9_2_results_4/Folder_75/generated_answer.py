def palindromes_between_indices(string):
    letters = string[2:5]
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                word = a + b + c
                if word == word[::-1]:
                    palindromes.add(word.lower())
    return palindromes