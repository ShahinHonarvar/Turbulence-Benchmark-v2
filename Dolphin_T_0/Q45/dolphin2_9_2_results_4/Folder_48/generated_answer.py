from itertools import permutations

def palindromes_between_indices(string):
    palindromes = set()
    substring = string[6:9]
    substring_length = len(substring)
    for perm in permutations(substring, substring_length):
        word = ''.join(perm).lower()
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes