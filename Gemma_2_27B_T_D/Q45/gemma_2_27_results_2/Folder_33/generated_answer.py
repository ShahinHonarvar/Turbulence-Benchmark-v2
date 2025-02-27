def palindromes_between_indices(text):
    letters = text[7:10]
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    word = a + b + c + d + d + c + b + a
                    if word.lower() == word[::-1].lower() and len(word) >= 4:
                        palindromes.add(word)
    return palindromes