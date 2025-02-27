from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:6].lower()
    result = set()
    for length in range(6, len(s) + 1):
        for p in permutations(s, length):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result