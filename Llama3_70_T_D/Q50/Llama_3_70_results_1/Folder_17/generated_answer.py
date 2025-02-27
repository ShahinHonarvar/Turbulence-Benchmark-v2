from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    anagram_count = 0
    for s in strings:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            anagram_map[sorted_str].append(s_lower)
    for anagrams in anagram_map.values():
        anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count >= 97