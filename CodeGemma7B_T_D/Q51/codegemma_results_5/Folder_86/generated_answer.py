from collections import defaultdict

def if_contains_anagrams(str_lst):
    anagrams = defaultdict(list)
    for string in str_lst:
        key = ''.join(sorted(string.lower()))
        if key not in anagrams or len(anagrams[key]) >= len(string):
            anagrams[key].append(string)
    return len(list(filter(lambda lst: len(lst) >= 3, anagrams.values()))) <= 48