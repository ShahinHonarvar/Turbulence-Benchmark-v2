from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s].append(s)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagram_count.values() if len(v) > 1))
    return pairs >= 277