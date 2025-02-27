from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    pair_count = 0
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_string(s)
            anagram_count[sorted_s] += 1
            pair_count += anagram_count[sorted_s] - 1
    return pair_count >= 25