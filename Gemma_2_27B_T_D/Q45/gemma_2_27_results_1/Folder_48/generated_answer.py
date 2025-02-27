def palindromes_between_indices(s):
    letters = s[6:9]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if len(word) >= 4 and word.lower() == word.lower()[::-1]:
            palindromes.add(word)
    return palindromes