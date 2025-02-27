def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:10] if char.isalpha()]
    possible_palindromes = set()
    if len(letters) < 3:
        return possible_palindromes
    for i in range(len(letters)):
        combinations = itertools.combinations_with_replacement(letters, i + 3)
        for combination in combinations:
            word = ''.join(combination)
            if word == word[::-1]:
                possible_palindromes.add(word)
    return possible_palindromes