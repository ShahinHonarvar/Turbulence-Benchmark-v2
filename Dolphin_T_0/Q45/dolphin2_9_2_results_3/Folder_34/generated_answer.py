def palindromes_between_indices(s):
    letters = s[5:8].lower()
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                for d in letters:
                    word = a + b + c + d
                    if word == word[::-1]:
                        palindromes.add(word)
    return palindromes