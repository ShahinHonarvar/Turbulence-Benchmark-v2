def palindromes_between_indices(string):
    letters_between = ''.join(sorted(string[1:9].lower()))
    palindromes = set()
    for i in range(4, len(letters_between) + 1):
        for combo in itertools.combinations(letters_between, i):
            word = ''.join(combo)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes