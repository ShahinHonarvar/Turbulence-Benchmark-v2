from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_map = defaultdict(list)
    count = 0
    for string in lst:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_map[sorted_str].append(string)
    for anagrams in anagram_map.values():
        n = len(anagrams)
        if n > 1:
            count += n * (n - 1) // 2
        if count > 147:
            return False
    return True