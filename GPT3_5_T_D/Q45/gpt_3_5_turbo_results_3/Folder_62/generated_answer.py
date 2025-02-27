import itertools
    import string

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    palindromes = set()
    for combo in itertools.permutations(letters, 9):
        if combo[:9] == combo[:9][::-1]:
            palindromes.add(''.join(combo)[:9])
    return palindromes