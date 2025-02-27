def palindromes_between_indices(s):
    indices = range(4, 10)
    letters = [s[i] for i in indices]
    palindromes = set()
    for p in permutations(letters, len(letters)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word.lower())
    return palindromes