from collections import defaultdict
    from itertools import combinations

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        anagrams[''.join(sorted(word.lower()))].append(word)
    pairs = sum((len(v) >= 3 for v in anagrams.values()))
    return pairs >= 66