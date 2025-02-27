from collections import defaultdict

def if_contains_anagrams(strings):

    def sorted_form(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            anagram_count[sorted_form(s)] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs >= 276