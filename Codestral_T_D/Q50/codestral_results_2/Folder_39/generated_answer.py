from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_map = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_map[''.join(sorted(s.lower()))].append(s)
    anagram_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_map.values()))
    return anagram_count >= 54