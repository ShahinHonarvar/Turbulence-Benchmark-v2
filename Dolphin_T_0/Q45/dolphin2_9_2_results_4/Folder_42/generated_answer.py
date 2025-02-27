from itertools import permutations

def palindromes_between_indices(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    sub_s = s[6:10]
    palindromes = set()
    for p in permutations(sub_s, 3):
        word = ''.join(p).lower()
        if word == word[::-1] and all((c in letters for c in word)):
            palindromes.add(word)
    return palindromes