from itertools import permutations 

def palindromes_between_indices(s):
    s = s[:6].lower()
    palindromes = set()
    for perm in permutations(s, 3):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    for perm in permutations(s, 4):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    for perm in permutations(s, 5):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    for perm in permutations(s, 6):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes