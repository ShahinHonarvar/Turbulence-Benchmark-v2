from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    anagram_count = 0
    for s in string_list:
        cleaned_s = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned_s) >= 3:
            sorted_s = ''.join(sorted(cleaned_s))
            anagram_dict[sorted_s].append(s)
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            anagram_count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return anagram_count <= 17