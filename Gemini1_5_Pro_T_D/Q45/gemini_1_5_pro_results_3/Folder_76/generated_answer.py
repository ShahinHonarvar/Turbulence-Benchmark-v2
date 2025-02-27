def palindromes_between_indices(string):
    letters = set([string[i].lower() for i in range(1, 5) if string[i].isalpha()])
    palindromes = set()
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    word = i + j + k + l
                    if word == word[::-1] and len(word) >= 4:
                        palindromes.add(word)
    return palindromes