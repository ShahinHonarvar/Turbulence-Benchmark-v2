from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str].append(s)
    for words in anagram_map.values():
        pair_count = len(words) * (len(words) - 1) // 2
        anagram_count += pair_count
        if anagram_count >= 17:
            return True
    return False