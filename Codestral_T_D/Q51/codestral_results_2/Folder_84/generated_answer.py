from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagram_map[key].append(s)
    anagram_pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_map.values()))
    return anagram_pairs <= 16