from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_map[sorted_s].append(s)
    count = 0
    for anagram_list in anagram_map.values():
        num_anagrams = len(anagram_list)
        if num_anagrams > 1:
            count += num_anagrams * (num_anagrams - 1) // 2
        if count >= 178:
            return True
    return False