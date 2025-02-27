from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_dict = defaultdict(list)
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        anagram_dict[sorted_str].append(s)
    count = 0
    for v in anagram_dict.values():
        if len(v) > 1 and len(v[0]) >= 3:
            count += len(v) * (len(v) - 1) // 2
    return count >= 155