from collections import defaultdict

def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            key = canonical_form(string)
            anagram_map[key].append(string)
    anagram_pair_count = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_map.values()))
    return anagram_pair_count <= 10