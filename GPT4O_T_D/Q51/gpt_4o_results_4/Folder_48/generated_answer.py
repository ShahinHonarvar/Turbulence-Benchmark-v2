from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        sorted_str = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(sorted_str) >= 3:
            anagram_map[sorted_str].append(string)
    anagram_pairs = 0
    for anagram_list in anagram_map.values():
        n = len(anagram_list)
        anagram_pairs += n * (n - 1) // 2
        if anagram_pairs > 277:
            return False
    return True