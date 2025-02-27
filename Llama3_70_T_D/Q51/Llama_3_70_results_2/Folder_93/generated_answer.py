from collections import defaultdict
from typing import List

def if_contains_anagrams(strings: List[str]) -> bool:
    anagrams_count = defaultdict(int)
    for string in strings:
        lower_string = string.lower()
        sorted_string = ''.join(sorted(filter(str.isalpha, lower_string)))
        if len(sorted_string) >= 3:
            anagrams_count[sorted_string] += 1
    return sum((count - 1 for count in anagrams_count.values() if count > 1)) <= 36