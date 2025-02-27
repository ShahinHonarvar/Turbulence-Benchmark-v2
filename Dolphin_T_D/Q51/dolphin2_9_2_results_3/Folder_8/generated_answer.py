from collections import Counter

def if_contains_anagrams(lst):

    def get_normal_form(s):
        return ''.join(sorted(s.lower()))
    counter = Counter()
    for s in lst:
        if len(s) >= 3:
            counter[get_normal_form(s)] += 1
    return sum((v * (v - 1) // 2 for v in counter.values())) <= 68