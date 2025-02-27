from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for p in permutations(list(string[5:10])):
        s = ''.join(p)
        if len(s) >= 5 and s.lower() == s[::-1].lower():
            result.add(s.lower())
    return result