def palindromes_between_indices(s):
    letters = set(s[3:9]) - set(' ')
    palindromes = set()
    for length in range(7, len(s[3:9]) + 1):
        for subset in combinations(letters, length):
            word = ''.join(sorted(list(''.join(subset))))
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes