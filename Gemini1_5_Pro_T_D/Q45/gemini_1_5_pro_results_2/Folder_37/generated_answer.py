def palindromes_between_indices(text):
    letters = set()
    for i in range(1, 5):
        if text[i].isalpha():
            letters.add(text[i].lower())
    palindromes = set()
    for l1 in letters:
        for l2 in letters:
            for l3 in letters:
                for l4 in letters:
                    for l5 in letters:
                        word = l1 + l2 + l3 + l4 + l5
                        if word == word[::-1] and len(word) >= 5:
                            palindromes.add(word)
    return palindromes