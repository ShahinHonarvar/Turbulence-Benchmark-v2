from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letters = ''.join(filter(str.isalpha, s))
    result = set()
    for r in range(3, len(letters) + 1):
        for p in permutations(letters, r):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result