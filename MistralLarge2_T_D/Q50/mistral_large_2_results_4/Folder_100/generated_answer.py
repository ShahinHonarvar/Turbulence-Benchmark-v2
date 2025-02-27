from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagram_dict[sorted_s].append(s)
    count_pairs = 0
    for group in anagram_dict.values():
        n = len(group)
        if n > 1:
            count_pairs += n * (n - 1) // 2
    return count_pairs >= 95