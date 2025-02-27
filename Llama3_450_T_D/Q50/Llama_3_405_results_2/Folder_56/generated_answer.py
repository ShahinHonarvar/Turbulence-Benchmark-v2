from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].append(s)
    anagram_count = 0
    for v in anagram_dict.values():
        anagram_count += len(v) * (len(v) - 1) // 2
    return anagram_count >= 77