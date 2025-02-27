from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and all((c.isalpha() for c in sorted_str)):
            anagram_dict[sorted_str].append(s)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values()))
    return anagram_count <= 147