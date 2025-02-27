from itertools import permutations

def palindromes_between_indices(s):
    str = ''.join(s[1:4].lower())
    palindromes = set()
    for p in permutations(str, 4):
        word = ''.join(p)
        if word == word[::-1] and word not in palindromes:
            palindromes.add(word)
    return palindromes