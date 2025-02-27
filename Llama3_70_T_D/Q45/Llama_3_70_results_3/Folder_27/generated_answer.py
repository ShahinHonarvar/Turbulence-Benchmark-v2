from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    s = ''.join(filter(str.isalpha, s))
    pals = set()
    for length in range(6, len(s) + 1):
        for p in permutations(s, length):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 6:
                pals.add(word)
    return pals