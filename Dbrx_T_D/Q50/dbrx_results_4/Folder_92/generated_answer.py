from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for string in string_list:
        anagrams[''.join(sorted(string.lower()))].append(string)
    return any((len(strings) >= 3 for strings in anagrams.values()))