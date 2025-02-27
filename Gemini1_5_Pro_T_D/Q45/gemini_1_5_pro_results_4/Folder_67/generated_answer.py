from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    s = string[2:7].lower()
    for p in permutations(s):
        if len(set(p).intersection({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'})) == 0:
            continue
        t = ''.join(p)
        if len(t) >= 5 and t == t[::-1]:
            result.add(t)
    return result