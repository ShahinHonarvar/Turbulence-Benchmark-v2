def palindromes_between_indices(text):
    letters = set([c.lower() for c in text[1:5] if c.isalpha()])
    palindromes = set()
    for i in letters:
        for j in letters:
            for k in letters:
                for l in letters:
                    for m in letters:
                        word = i + j + k + l + m
                        if word == word[::-1] and len(word) >= 5:
                            palindromes.add(word)
    return palindromes