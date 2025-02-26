from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in string_list:
        filtered_s = ''.join(filter(str.isalpha, s.lower()))
        if len(filtered_s) >= 3:
            sorted_s = ''.join(sorted(filtered_s))
            anagram_dict[sorted_s].append(s)
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
            if anagram_count > 38:
                return False
    return True