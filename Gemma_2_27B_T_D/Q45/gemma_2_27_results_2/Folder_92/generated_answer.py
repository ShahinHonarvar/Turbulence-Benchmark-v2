def palindromes_between_indices(text):
    letters = text[4:8].lower()
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes