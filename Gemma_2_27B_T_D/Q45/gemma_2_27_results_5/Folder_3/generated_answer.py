def palindromes_between_indices(s):
    letters = s[7:10]
    palindromes = set()
    for word in permutations(letters):
        word = ''.join(word)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes