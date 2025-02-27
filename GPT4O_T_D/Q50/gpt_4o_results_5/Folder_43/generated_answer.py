from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_groups = defaultdict(int)
    for s in str_list:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_groups[sorted_s] += 1
    count = 0
    for value in anagram_groups.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count >= 61:
            return True
    return False