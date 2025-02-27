from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        str_dict[tuple(sorted(s.lower()))].append(s)
    anagram_count = 0
    for anagram_list in str_dict.values():
        for i in range(len(anagram_list)):
            for j in range(i + 1, len(anagram_list)):
                anagram_count += 1
    return anagram_count >= 67