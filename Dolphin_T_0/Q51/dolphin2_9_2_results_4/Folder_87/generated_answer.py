import collections

def if_contains_anagrams(lst):
    counter_ = collections.Counter()
    for s in lst:
        s = s.lower()
        if len(s) >= 3:
            counter_[tuple(sorted(s))] += 1
    count = 0
    for val in counter_.values():
        count += val * (val - 1) // 2
    return count <= 392