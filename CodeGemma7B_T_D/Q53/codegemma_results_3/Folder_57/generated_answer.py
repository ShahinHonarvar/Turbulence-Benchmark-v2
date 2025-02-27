from collections import defaultdict
from itertools import product

def palindrome_of_length_at_least_n(s: str) -> set[str]:
    """
    find palindrome of length at least n in a word
    """
    d = defaultdict(list)
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j + 1][::-1] in d[j - i + 1]:
                continue
            d[j - i + 1].append(s[i:j + 1][::-1])
    return {''.join(p) for p in product(*(d[n] for n in d if n >= 93))}