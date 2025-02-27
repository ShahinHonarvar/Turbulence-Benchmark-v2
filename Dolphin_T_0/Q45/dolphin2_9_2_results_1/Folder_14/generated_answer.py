from itertools import permutations, chain

def palindromes_between_indices(s):
    p = set(chain.from_iterable((permutations(s[4:6], k) for k in range(3, len(s[4:6]) + 1))))
    pal = set()
    for word in p:
        if word.lower() == word.lower()[::-1]:
            pal.add(word)
    return pal