def palindromes_between_indices(text):
    letters = text[2:5]
    palindromes = set()
    for letter1 in letters:
        for letter2 in letters:
            for letter3 in letters:
                for letter4 in letters:
                    candidate = ''.join([letter1, letter2, letter3, letter4]).lower()
                    if candidate == candidate[::-1]:
                        palindromes.add(candidate)
    return palindromes