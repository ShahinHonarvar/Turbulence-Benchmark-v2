from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counter = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            counter[normalize(s)] += 1
    pair_count = 0
    for count in counter.values():
        pair_count += count * (count - 1) // 2
    return pair_count >= 25