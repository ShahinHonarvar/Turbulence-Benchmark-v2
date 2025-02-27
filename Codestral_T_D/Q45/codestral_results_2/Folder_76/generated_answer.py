from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    substring = string[1:5].lower()
    for perm in permutations(substring):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes