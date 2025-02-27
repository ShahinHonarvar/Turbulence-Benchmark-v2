from collections import defaultdict

def if_contains_anagrams(strings):
    sorted_strings = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        sorted_strings[sorted_s].append(s)
    anagram_pairs = 0
    for group in sorted_strings.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs <= 58