import itertools

def palindromes_between_indices(string):
    english_letters = [ch for ch in string if ch.isalpha()]
    english_letters = list(set(english_letters))
    english_letters.sort()
    combinations = itertools.combinations(english_letters, 7)
    palindromes = set()
    for combination in combinations:
        palindromes.update([''.join(combination).lower(), ''.join(combination).upper()])
    return palindromes