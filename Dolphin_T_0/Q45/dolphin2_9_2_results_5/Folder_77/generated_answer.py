def palindromes_between_indices(s):
    letters = s[4:7]
    palindromes = set()
    permutations = set((''.join(p) for p in permutations(letters)))
    for word in permutations:
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word.lower())
    return palindromes