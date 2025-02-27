def palindromes_between_indices(string):
    letters = set(filter(str.isalpha, string[4:8]))
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    word = a + b + c + d
                    if word == word[::-1]:
                        palindromes.add(word.lower())
    return palindromes