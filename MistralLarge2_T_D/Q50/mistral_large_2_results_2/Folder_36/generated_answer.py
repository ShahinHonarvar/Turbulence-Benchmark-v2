from collections import defaultdict

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    str_dict = defaultdict(list)
    for s in lst:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        str_dict[sorted_str].append(s)
    for group in str_dict.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count >= 312