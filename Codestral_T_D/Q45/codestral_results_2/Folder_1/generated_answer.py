from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:8].lower()
    palindromes = set()
    for perm in permutations(s):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes