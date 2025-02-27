from collections import defaultdict

def if_contains_anagrams(str_list):

    def find_anagrams(str):
        sorted_str = ''.join(sorted(str.lower()))
        return defaultdict(list).setdefault(sorted_str, []).append(str)
    anagrams = defaultdict(list)
    for string in str_list:
        if len(string) >= 3:
            find_anagrams(string)
    pairs = 0
    for group in anagrams.values():
        pairs += len(group) * (len(group) - 1) // 2
    return pairs >= 42