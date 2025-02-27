from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str].append(s)
    for anagram_list in anagram_map.values():
        if len(anagram_list) > 1:
            n = len(anagram_list)
            count += n * (n - 1) // 2
            if count >= 29:
                return True
    return False