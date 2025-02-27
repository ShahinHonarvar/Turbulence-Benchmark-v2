def palindromes_between_indices(text):
    letters = text[5:8]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    candidate = letter1 + letter2 + letter3 + letter4 + letter4 + letter3 + letter2 + letter1
                    if candidate.lower() == candidate[::-1].lower() and len(candidate) >= 4:
                        palindromes.add(candidate)
    return palindromes