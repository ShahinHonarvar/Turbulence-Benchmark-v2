from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams_count = 0
    frequency = defaultdict(int)
    for s in lst:
        if len(s) >= 3:
            sorted_tuple = tuple(sorted(s.lower()))
            frequency[sorted_tuple] += 1
    for count in frequency.values():
        if count > 1:
            anagrams_count += count * (count - 1) // 2
    return anagrams_count <= 173