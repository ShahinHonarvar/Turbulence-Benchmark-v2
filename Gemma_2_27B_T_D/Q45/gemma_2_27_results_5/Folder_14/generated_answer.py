def palindromes_between_indices(text):
    substring = text[4:6]
    letters = ''.join((c for c in substring if c.isalpha()))
    palindromes = set()
    for perm in permutations(letters):
        word = ''.join(perm)
        if word.lower() == word[::-1].lower() and len(word) >= 3:
            palindromes.add(word)
    return palindromes