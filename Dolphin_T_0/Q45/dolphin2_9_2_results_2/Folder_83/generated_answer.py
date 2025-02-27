import itertools
    from collections import Counter

def palindromes_between_indices(s):
    s = s[2:10]
    counter = Counter(s.lower())
    letters = list(counter.keys())
    n = len(s)
    palindromes = {''.join(i) for i in itertools.product(letters, repeat=n) if ''.join(i).lower() == ''.join(i).lower()[::-1]}
    return set([p for p in palindromes if len(p) >= 7])