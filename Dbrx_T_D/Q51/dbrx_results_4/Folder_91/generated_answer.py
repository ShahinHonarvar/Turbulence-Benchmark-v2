import collections

def if_contains_anagrams(list_of_strings):
    anagrams = collections.defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    pair_count = sum((1 for group in anagrams.values() if len(group) >= 3))
    return pair_count <= 88