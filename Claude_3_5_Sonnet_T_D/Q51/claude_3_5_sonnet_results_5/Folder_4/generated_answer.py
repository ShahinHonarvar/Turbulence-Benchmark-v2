from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = defaultdict(list)
    for s in string_list:
        cleaned = ''.join(filter(str.isalpha, s.lower()))
        if len(cleaned) >= 3:
            sorted_str = ''.join(sorted(cleaned))
            anagram_dict[sorted_str].append(s)
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            anagram_count += len(anagrams) * (len(anagrams) - 1) // 2
    return anagram_count <= 84