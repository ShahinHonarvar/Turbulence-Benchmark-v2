from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_dict[sorted_s].append(s)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_dict.values() if len(v) > 1))
    return anagram_pairs <= 28