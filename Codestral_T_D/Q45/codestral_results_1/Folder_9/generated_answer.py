from itertools import permutations

def palindromes_between_indices(string):
    string = string.lower()
    length = len(string)
    if length < 7:
        return set()
    string = string[:7]
    palindromes = set()
    for perm in permutations(string, length):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes