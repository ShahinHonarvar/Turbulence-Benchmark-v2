def palindromes_between_indices(s):
    palindromes = set()
    string_between_indices = s[1:8]
    english_letters = [c for c in string_between_indices if c.isalpha()]
    for i in range(6, len(english_letters) + 1):
        permutations = itertools.permutations(english_letters, i)
        for permutation in permutations:
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes