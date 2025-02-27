from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = defaultdict(list)
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagram_pairs[sorted_str].append(s)
    count = 0
    for group in anagram_pairs.values():
        if len(group) > 1:
            count += len(group) * (len(group) - 1) // 2
    return count <= 38