from itertools import permutations

def palindromes_between_indices(s):
    result = set()
    substring = s[3:5].lower()
    for perm in permutations(substring):
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 3:
            result.add(word)
    return result