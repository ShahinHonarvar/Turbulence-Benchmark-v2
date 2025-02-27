from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_map[sorted_str].append(s)
    anagram_pairs = 0
    for anagrams in anagram_map.values():
        if len(anagrams) > 1:
            n = len(anagrams)
            anagram_pairs += n * (n - 1) // 2
            if anagram_pairs >= 30:
                return True
    return False