from typing import List
from collections import defaultdict

def if_contains_anagrams(strings: List[str]) -> bool:
    anagrams = defaultdict(int)
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        anagrams[sorted_str] += 1
    return sum((count - 1 for count in anagrams.values())) >= 96