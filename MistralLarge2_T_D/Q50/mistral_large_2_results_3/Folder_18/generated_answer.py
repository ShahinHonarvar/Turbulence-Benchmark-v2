from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    str_dict = defaultdict(list)
    for s in lst:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        str_dict[sorted_s].append(s)
    for key in str_dict:
        if len(str_dict[key]) > 1:
            anagram_count += len(str_dict[key]) * (len(str_dict[key]) - 1) // 2
    return anagram_count >= 106