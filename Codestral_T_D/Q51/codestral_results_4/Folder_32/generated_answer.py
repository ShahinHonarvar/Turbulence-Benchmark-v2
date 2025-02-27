from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagrams[key].append(s)
    return sum((len(anagrams[key]) * (len(anagrams[key]) - 1) // 2 for key in anagrams)) <= 89