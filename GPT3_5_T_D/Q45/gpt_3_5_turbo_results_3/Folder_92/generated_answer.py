import itertools
    import string as s

def palindromes_between_indices(string):
    substrings = set(string[4:8])
    for length in range(4, 8):
        substrings.union((set(''.join(subset)) for subset in itertools.permutations(string[4:8], length)))
    palindromes = {word for word in substrings if word.lower() == word.lower()[::-1]}
    return palindromes