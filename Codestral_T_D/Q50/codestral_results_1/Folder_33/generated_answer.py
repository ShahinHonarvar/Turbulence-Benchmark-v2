def if_contains_anagrams(strings):
    anagram_count = {}
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if len(sorted_s) >= 3:
            anagram_count[sorted_s] = anagram_count.get(sorted_s, 0) + 1
    pair_count = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pair_count >= 140