def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:9] if c.isalpha()]
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes