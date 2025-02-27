from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            d[''.join(sorted(word.lower()))].append(word)
    return sum([len(anagrams) * (len(anagrams) - 1) for anagrams in d.values()]) / 2 >= 75