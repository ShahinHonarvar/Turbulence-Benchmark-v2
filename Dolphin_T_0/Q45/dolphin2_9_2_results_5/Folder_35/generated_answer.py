from itertools import permutations

def palindromes_between_indices(string):
    substring = string[2:5]
    palindromes = set()
    for p in permutations(substring, len(substring)):
        word = ''.join(p).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes