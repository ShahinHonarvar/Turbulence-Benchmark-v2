from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagrams = defaultdict(lambda: [])
    for str_ in list_of_strings:
        if len(str_) < 3:
            continue
        sorted_str = ''.join(sorted(str_.lower()))
        anagrams[sorted_str].append(str_)
    count = 0
    for k, v in anagrams.items():
        count += len(v) * (len(v) - 1) // 2
        if count > 81:
            return True
    return False