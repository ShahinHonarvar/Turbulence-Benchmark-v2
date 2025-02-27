def palindromes_between_indices(text):
    letters = text[4:8].lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes