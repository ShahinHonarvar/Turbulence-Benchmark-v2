from itertools import permutations

def palindromes_between_indices(s):
    letters = s[5:8]
    palindromes = set()
    for permutation in permutations(letters):
        word = ''.join(permutation)
        if word.lower() == word.lower()[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes