import itertools

def palindromes_between_indices(string):
    s = set()
    for permutation in itertools.permutations(string[4:10]):
        word = ''.join(permutation)
        if len(word) >= 7 and word.lower() == word[::-1].lower():
            s.add(word.lower())
    return s