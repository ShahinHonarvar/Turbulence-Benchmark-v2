from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    letters = [c for c in s[1:8] if c.isalpha()]
    set_of_palindromes = set()
    for r in range(6, len(letters) + 1):
        for perm in permutations(letters, r):
            word = ''.join(perm)
            if word == word[::-1]:
                set_of_palindromes.add(word)
    return set_of_palindromes