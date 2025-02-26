from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        cleaned = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned) >= 3:
            sorted_str = ''.join(sorted(cleaned))
            anagram_dict[sorted_str].append(s)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_dict.values()))
    return anagram_pairs <= 17