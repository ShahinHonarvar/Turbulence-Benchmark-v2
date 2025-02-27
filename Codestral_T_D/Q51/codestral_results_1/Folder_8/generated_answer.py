from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        if len(word) < 3:
            continue
        key = ''.join(sorted(word.lower()))
        d[key].append(word)
    pair_count = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return pair_count <= 68