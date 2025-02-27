from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    length = len(s)
    palindromes = set()
    if length < 7:
        return palindromes
    for perm in permutations(s, length):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes