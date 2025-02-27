def palindromes_between_indices(text):
    letters = text[7:9].lower()
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes