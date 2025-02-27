import itertools

def palindromes_between_indices(string):
    if len(string) < 6:
        return set()
    letters = string[:6].lower()
    permutations = list(itertools.permutations(letters, 6))
    palindromes = set()
    for permutation in permutations:
        word = ''.join(permutation)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes