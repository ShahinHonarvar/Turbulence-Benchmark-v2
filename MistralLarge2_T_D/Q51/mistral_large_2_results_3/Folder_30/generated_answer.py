from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_str(s)
            anagram_dict[sorted_s].append(s)
    anagram_pairs = sum((1 for pair in anagram_dict.values() if len(pair) > 1))
    return anagram_pairs <= 28