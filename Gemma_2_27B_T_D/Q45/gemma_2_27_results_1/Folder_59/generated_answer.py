def palindromes_between_indices(text):
    letters = text[8:10]
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes