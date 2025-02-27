def if_contains_anagrams(lst):
    anagram_count = {}
    for s in lst:
        if len(s) < 3:
            continue
        s = ''.join(filter(str.isalpha, s)).lower()
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_count:
            anagram_count[sorted_s] += 1
        else:
            anagram_count[sorted_s] = 1
    pairs = 0
    for count in anagram_count.values():
        pairs += count * (count - 1) // 2
    return pairs <= 94