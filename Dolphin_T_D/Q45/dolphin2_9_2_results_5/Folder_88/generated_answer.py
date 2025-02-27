def palindromes_between_indices(s):
    substring = s[3:8]
    letters = ''.join([c for c in substring if c.isalpha()])
    if len(letters) < 3:
        return set()
    letters = letters.lower()
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes