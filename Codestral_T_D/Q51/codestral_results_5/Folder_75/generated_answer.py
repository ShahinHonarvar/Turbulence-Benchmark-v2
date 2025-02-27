from collections import Counter

def if_contains_anagrams(str_list):
    anagram_count = 0
    anagram_dict = {}
    for s in str_list:
        lower_s = s.lower()
        if len(lower_s) >= 3:
            key = ''.join(sorted(lower_s))
            anagram_dict[key] = anagram_dict.get(key, 0) + 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count <= 55