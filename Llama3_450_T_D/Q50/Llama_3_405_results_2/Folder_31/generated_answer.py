from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            anagram_dict[sorted_str].append(s)
    anagram_count = sum((len(value) * (len(value) - 1) // 2 for value in anagram_dict.values()))
    return anagram_count >= 68