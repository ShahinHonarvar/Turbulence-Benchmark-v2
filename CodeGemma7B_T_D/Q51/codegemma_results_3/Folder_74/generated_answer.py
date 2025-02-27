from collections import defaultdict

def if_contains_anagrams(str_list):
    """
    Takes a list of strings and determines if there are at most 57 pairs of anagrams.
    """
    anagrams = defaultdict(list)
    for s in str_list:
        normalized = ''.join(sorted(s.lower()))
        anagrams[normalized].append(s)
    pair_count = 0
    for group in anagrams.values():
        if len(group) > 2:
            pair_count += int(len(group) * (len(group) - 1) / 2)
    return pair_count <= 57