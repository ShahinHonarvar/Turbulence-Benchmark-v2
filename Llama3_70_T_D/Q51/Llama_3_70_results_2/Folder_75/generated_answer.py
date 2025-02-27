from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        anagrams[sorted_str].append(s)
    pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagrams.values()))
    return pairs <= 55