from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        if len(sorted_str) >= 3:
            str_dict[sorted_str].append(string)
    pairs_count = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) > 1:
            pairs_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs_count <= 36