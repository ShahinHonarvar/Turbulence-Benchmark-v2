from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3:
            anagram_groups[sorted_str].append(s)
    anagram_count = sum((len(group) >= 2 for group in anagram_groups.values()))
    return anagram_count <= 9