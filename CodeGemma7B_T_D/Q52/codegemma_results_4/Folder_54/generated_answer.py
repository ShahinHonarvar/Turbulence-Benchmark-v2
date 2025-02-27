def palindrome_of_length_n(str):
    if len(str) < 85:
        return set()
    ns = [c for c in str if c.isalpha()]
    return {''.join(n) for n in permutations(ns, 85)}