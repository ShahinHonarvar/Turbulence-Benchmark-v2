def palindromes_between_indices(string):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    substring = set(string[2:6].lower())
    palindromes = set()
    for length in range(5, len(substring) + 1):
        for combination in itertools.combinations(substring, length):
            word = ''.join(combination)
            if word == word[::-1] and set(word).issubset(english_letters):
                palindromes.add(word)
    return palindromes