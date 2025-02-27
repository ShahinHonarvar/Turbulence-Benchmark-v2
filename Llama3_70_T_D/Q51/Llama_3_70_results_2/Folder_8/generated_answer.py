def if_contains_anagrams(lst):
    anagram_count = {}
    for s in lst:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_count:
            anagram_count[sorted_s] += 1
        else:
            anagram_count[sorted_s] = 1
    count = 0
    for v in anagram_count.values():
        if v > 1:
            count += v * (v - 1) // 2
    return count <= 68