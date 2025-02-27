from itertools import permutations

def palindromes_between_indices(s):
    letters_between = s[1:7]
    palindromes = set()
    for p in permutations(set(letters_between.lower()), 4):
        word = ''.join(p)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes