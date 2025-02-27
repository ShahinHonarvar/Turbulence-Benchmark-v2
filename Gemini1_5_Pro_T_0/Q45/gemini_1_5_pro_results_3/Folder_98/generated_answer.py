from itertools import permutations

def palindromes_between_indices(string):
    s = set()
    for p in permutations(string[3:6]):
        candidate = ''.join(p)
        if len(candidate) >= 4 and candidate.lower() == candidate[::-1].lower():
            s.add(candidate.lower())
    return s