from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[7:10].lower()
    letters = [ch for ch in substring if ch.isalpha()]
    result = set()
    for length in range(4, len(letters) + 1):
        perm_set = set((''.join(p) for p in permutations(letters, length)))
        for word in perm_set:
            if word == word[::-1]:
                result.add(word)
    return result