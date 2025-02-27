from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            anagram_dict[norm].append(s)
    anagram_pairs = 0
    for group in anagram_dict.values():
        if len(group) > 1:
            anagram_pairs += len(group) - 1
    return anagram_pairs <= 26