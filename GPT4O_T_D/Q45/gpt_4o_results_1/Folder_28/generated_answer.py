from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:6] if c.isalpha()]
    palindromes = set()
    for i in range(4, 6):
        for perm in permutations(chars, i):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes