from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s] += 1
    count = 0
    for value in anagram_dict.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count >= 67:
            return True
    return False