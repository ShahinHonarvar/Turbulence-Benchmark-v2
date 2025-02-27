from itertools import permutations

def palindromes_between_indices(s):
    chars = s[6:9].lower()
    palindromes = set()
    for p in permutations(chars, 4):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes