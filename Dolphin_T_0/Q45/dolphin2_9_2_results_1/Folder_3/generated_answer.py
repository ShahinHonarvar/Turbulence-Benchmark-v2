def palindromes_between_indices(s):
    indices = range(7, 10)
    subset = ''.join([ch for i, ch in enumerate(s) if i in indices])
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for word in English_letters.combinations(subset, 3, ' '):
        if word == word[::-1]:
            palindromes.add(word.lower())
    return palindromes