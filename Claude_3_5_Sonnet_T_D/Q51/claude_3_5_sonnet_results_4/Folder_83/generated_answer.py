from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_groups = defaultdict(list)
    for s in string_list:
        cleaned = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned) >= 3:
            sorted_s = ''.join(sorted(cleaned))
            anagram_groups[sorted_s].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs <= 19