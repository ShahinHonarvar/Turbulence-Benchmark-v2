def palindromes_between_indices(s):
    letters = set((s[i].lower() for i in range(1, 6) if s[i].isalpha()))
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for p in itertools.permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1] and len(set(word)) > 1:
                palindromes.add(word)
    return palindromes