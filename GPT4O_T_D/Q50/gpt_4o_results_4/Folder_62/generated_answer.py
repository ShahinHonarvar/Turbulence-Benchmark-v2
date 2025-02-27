from collections import defaultdict

def if_contains_anagrams(lst):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    counter = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            counter[sorted_str(s)] += 1
    anagram_pairs = 0
    for count in counter.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 43:
                return True
    return False