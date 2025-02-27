from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    pairs = 0
    for group in anagrams.values():
        if len(group) >= 3:
            pairs += len(group) * (len(group) - 1) // 2
    return pairs >= 17