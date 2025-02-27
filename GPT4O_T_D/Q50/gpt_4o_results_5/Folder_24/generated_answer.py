from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagram_map[sorted_str].append(string)
    anagram_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_map.values() if len(lst) > 1))
    return anagram_count >= 65