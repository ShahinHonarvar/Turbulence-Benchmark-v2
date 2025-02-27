from itertools import permutations

def palindromes_between_indices(string):
    string = string[1:6].lower()
    palindromes = set()
    for perm in permutations(string):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 6:
            palindromes.add(word)
    return palindromes