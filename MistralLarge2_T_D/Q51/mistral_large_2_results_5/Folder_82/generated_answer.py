from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    anagram_pairs = [v for v in anagram_dict.values() if len(v) > 1 and len(v[0]) >= 3]
    return len(anagram_pairs) <= 40