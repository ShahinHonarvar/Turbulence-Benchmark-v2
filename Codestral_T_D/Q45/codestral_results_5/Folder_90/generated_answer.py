from itertools import permutations

def palindromes_between_indices(s):
    s = s[0:6].lower()
    lengths = range(4, len(s) + 1)
    palindromes = set()
    for length in lengths:
        for perm in permutations(s, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes