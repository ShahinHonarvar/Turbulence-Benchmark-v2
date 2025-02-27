import itertools

def palindromes_between_indices(string):
    s = string[7:10]
    s = ''.join((ch for ch in s if ch.isalnum())).lower()
    p = set()
    for i in range(4, len(s) + 1):
        for item in itertools.permutations(s, i):
            word = ''.join(item)
            if word == word[::-1] and word not in p:
                p.add(word)
    return p