from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_dict = defaultdict(lambda: [])
    for str_ in list_of_strings:
        if len(str_) < 3:
            continue
        sorted_str = ''.join(sorted(str_.lower()))
        anagram_dict[sorted_str].append(str_)
    count = 0
    for key in anagram_dict:
        n = len(anagram_dict[key])
        count += n * (n - 1) / 2
    return count <= 276