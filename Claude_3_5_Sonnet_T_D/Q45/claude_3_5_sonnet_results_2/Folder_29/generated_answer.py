from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[2:10] if c.isalpha()))
    result = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result