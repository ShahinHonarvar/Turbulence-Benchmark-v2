from collections import defaultdict

def if_contains_anagrams(strings):

    def sort_str(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            sorted_form = sort_str(s)
            anagram_groups[sorted_form] += 1
    pairs = 0
    for count in anagram_groups.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 312