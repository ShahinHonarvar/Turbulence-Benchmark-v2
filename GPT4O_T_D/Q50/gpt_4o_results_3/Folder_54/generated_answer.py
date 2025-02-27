from collections import defaultdict

def if_contains_anagrams(strings):
    count = 0
    anagram_groups = defaultdict(int)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_groups[sorted_str] += 1
    for value in anagram_groups.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count >= 74:
            return True
    return False