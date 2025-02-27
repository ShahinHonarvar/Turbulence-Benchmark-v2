from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        str_lower = string.lower()
        sorted_str = ''.join(sorted(str_lower))
        if len(str_lower) >= 3:
            str_dict[sorted_str].append(str_lower)
    anagram_pairs = 0
    for _, anagrams in str_dict.items():
        anagram_pairs += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_pairs >= 219