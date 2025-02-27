from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_count = defaultdict(int)
    for item in lst:
        item_lower = ''.join(filter(str.isalpha, item)).lower()
        if len(item_lower) < 3:
            continue
        sorted_str = ''.join(sorted(item_lower))
        anagram_count[sorted_str] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 93