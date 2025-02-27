def if_contains_anagrams(lst):
    lst = [''.join(sorted(s.lower())) for s in lst if len(s) >= 3]
    anagram_count = {}
    for s in lst:
        if s in anagram_count:
            anagram_count[s] += 1
        else:
            anagram_count[s] = 1
    pairs = 0
    for count in anagram_count.values():
        if count > 1:
            pairs += count * (count - 1) // 2
    return pairs >= 91