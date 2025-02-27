from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagram_map[key] += 1
    count = 0
    for val in anagram_map.values():
        count += val * (val - 1) // 2
        if count >= 77:
            return True
    return False