from itertools import permutations

def palindromes_between_indices(s):
    s = s[5:8].lower()
    palindromes = set()
    for perm in permutations(s):
        word = ''.join(perm)
        if len(word) >= 4 and word == word[::-1]:
            palindromes.add(word)
    return palindromes