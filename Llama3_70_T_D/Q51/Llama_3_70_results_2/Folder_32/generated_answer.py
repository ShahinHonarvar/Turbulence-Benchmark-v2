def if_contains_anagrams(lst):
    anagram_count = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_count:
            anagram_count[sorted_s] += 1
        else:
            anagram_count[sorted_s] = 1
    pairs = sum([count * (count - 1) // 2 for count in anagram_count.values()])
    return pairs <= 89