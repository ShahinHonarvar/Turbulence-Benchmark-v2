from given string between indicies 6 and 9 inclusive

def palindromes_between_indices(x):
    """
    Return set of palindromes of length 4 or more
    """
    letters = list(x[6:10])
    letters.sort()
    polindromes = set()
    for w in itertools.permutations(letters):
        if ''.join(w).lower() not in polindromes:
            polindromes.add(''.join(w).lower())
    return polindromes