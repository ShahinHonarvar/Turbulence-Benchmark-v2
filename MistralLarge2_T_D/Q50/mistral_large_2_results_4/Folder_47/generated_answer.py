from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        anagram_count[sorted_s].append(s)
    count = 0
    for group in anagram_count.values():
        if len(group) > 1:
            count += len(group) - 1
    return count >= 47