import itertools

def palindromes_between_indices(s):
    s = s[4:6].lower()
    result = set()
    for r in range(3, len(s) + 1):
        for p in itertools.permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result