from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                result.add(word)
    return result