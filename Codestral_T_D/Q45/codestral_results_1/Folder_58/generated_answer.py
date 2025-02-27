from itertools import permutations

def palindromes_between_indices(s):
    s = s[:7].lower()
    palindromes = set()
    for p in permutations(s, 6):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes