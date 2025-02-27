import collections

def if_contains_anagrams(strings):
    anagrams = collections.defaultdict(list)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            anagrams[''.join(sorted(s))].append(s)
    return sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values())) <= 18