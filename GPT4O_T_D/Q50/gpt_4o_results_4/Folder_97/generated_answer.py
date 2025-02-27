def if_contains_anagrams(strings):
    anagram_map = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            if sorted_s in anagram_map:
                anagram_map[sorted_s] += 1
            else:
                anagram_map[sorted_s] = 1
    count_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            count_pairs += count * (count - 1) // 2
        if count_pairs >= 123:
            return True
    return False