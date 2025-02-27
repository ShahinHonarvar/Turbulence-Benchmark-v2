def if_contains_anagrams(lst):
    sorted_lsts = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    anagram_counts = {i: sorted_lsts.count(i) for i in sorted_lsts}
    return sum((v >= 2 for v in anagram_counts.values())) >= 89