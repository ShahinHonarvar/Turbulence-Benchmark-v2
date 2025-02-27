from itertools import product

def palindrome_of_length_at_least_n(s):
    return {''.join(p) for p in product(*([[c.lower(), c.upper()] for c in s if c.isalpha()] for _ in range(95))) if p == p[::-1]}