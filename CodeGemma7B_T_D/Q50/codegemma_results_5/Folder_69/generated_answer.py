from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for s in str_list:
        s = ''.join(sorted(s.lower()))
        str_dict[s].append(s)
    anagram_count = 0
    for anagrams in str_dict.values():
        n = len(anagrams)
        anagram_count += n * (n - 1) // 2
    return anagram_count >= 188