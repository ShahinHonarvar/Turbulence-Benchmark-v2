from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        key = ''.join(sorted(s.lower()))
        anagram_dict[key].append(s)
    pairs = sum((len(lst) * (len(lst) - 1) // 2 for lst in anagram_dict.values() if len(lst) > 1))
    return pairs >= 92