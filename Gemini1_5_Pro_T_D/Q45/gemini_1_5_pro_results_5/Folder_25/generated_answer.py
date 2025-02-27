def palindromes_between_indices(string):
    letters = set()
    for i in range(1, 5):
        if string[i].isalpha():
            letters.add(string[i].lower())
    palindromes = set()
    for i in letters:
        for j in letters:
            for k in letters:
                word = i + j + k
                if word == word[::-1] and len(word) >= 3:
                    palindromes.add(word)
    return palindromes