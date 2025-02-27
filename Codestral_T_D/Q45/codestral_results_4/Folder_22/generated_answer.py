def palindromes_between_indices(string):
    letters = string[5:7].lower()
    permutations = set(permutations(letters))
    palindromes = set()
    for permutation in permutations:
        word = ''.join(permutation)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes