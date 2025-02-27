from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(lambda: [])
    for str_ in list_of_strings:
        if len(str_) < 3:
            continue
        sorted_str = ''.join(sorted(str_.lower()))
        anagram_dict[sorted_str].append(str_)
    cnt = 0
    for key, val in anagram_dict.items():
        cnt += len(val) * (len(val) - 1) // 2
        if cnt > 401:
            return False
    return True