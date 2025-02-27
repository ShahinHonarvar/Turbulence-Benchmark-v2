def palindromes_between_indices(text):
    letters = set(text[1:7].lower())
    palindromes = set()
    for a in letters:
        for b in letters:
            for c in letters:
                if a != b and a != c and (b != c):
                    palindromes.add(a + b + c + c + b + a)
    return palindromes