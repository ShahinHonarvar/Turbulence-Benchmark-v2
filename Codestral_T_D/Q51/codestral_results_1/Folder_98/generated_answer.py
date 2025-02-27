from collections import defaultdict

def if_contains_anagrams(lst):
    d = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) >= 3:
            d[key].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in d.values()))
    return anagram_pairs <= 46