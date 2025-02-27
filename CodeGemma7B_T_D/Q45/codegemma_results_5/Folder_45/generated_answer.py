from itertools import permutations

def palindromes_between_indices(word):
    words = permutations(word[5:10], 5)
    palindromes = set()
    for w in words:
        if ''.join(w) == ''.join(w)[::-1]:
            palindromes.add(''.join(w).lower())
    return palindromes