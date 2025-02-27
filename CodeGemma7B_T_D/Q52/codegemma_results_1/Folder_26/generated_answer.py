from itertools import combinations

def palindrome_of_length_n(s):
    return {''.join(p) for p in combinations(s.lower(), 366) if p == p[::-1]}