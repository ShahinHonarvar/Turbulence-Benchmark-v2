from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_map[sorted_string].append(string)
    anagram_pairs_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_map.values()))
    return anagram_pairs_count >= 88