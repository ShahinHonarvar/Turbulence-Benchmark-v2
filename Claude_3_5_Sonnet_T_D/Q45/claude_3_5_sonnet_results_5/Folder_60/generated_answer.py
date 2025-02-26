from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:7] if c.isalpha()]
    result = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result