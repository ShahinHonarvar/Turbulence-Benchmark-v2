from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(int)
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_dict[sorted_s] += 1
    count = 0
    for val in anagram_dict.values():
        if val > 1:
            count += val * (val - 1) // 2
    return count >= 55