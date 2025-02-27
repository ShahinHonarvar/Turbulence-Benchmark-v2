import itertools
from typing import Set

def palindromes_between_indices(s: str) -> Set[str]:
    chars = [c for c in s[2:9] if c.isalpha()]
    return {''.join(p) for p in itertools.product(*chars + [c.lower() for c in chars]) if p == p[::-1] and len(p) >= 7}