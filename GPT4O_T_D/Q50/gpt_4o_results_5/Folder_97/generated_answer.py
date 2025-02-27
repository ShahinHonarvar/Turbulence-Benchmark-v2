from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_map[sorted_str] += 1
    count = 0
    for value in anagram_map.values():
        if value > 1:
            count += value * (value - 1) // 2
            if count >= 123:
                return True
    return False