from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_count[sorted_str].append(s)
    count_pairs = sum((len(v) >= 2 for v in anagram_count.values()))
    return count_pairs >= 123