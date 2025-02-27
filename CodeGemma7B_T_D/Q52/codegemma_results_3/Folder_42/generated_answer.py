from itertools import combinations

def palindrome_of_length_n(string):
    if len(string) < 279:
        return set()
    mod = len(string) - 279 + 1
    return set([''.join(c) for i in range(mod) for j in range(i + 279, len(string), mod) for c in combinations(list(string)[i:j], 279)])