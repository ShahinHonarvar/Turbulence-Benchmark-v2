from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    result = set()
    for i in range(7, len(letters) + 1):
        for perm in permutations(letters, i):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result