def palindromes_between_indices(text):
    letters = text[7:9].lower()
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes