from collections import defaultdict

def if_contains_anagrams(lst):
    sorted_str_count = defaultdict(int)
    for s in lst:
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s.lower()))
        sorted_str_count[sorted_s] += 1
    pairs = sum((count * (count - 1) // 2 for count in sorted_str_count.values() if count > 1))
    return pairs <= 17