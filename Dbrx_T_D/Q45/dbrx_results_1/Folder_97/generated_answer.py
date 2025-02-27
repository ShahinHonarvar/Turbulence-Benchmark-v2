def palindromes_between_indices(s):
    letters = set(s.lower()[0:5])
    palindromes = set()
    for letter in letters:
        palindromes.add(letter * 3)
        for other in letters - {letter}:
            palindromes.add(letter + other + letter)
    return {p for p in palindromes if len(p) >= 3}