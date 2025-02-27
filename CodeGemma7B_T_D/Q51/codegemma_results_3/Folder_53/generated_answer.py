from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        anagrams[key].append(string)
    count = 0
    for group in anagrams.values():
        count += len(group) - 1
    return count <= 8