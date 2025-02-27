def if_contains_anagrams(strings):
    anagram_dict = {}
    for s in strings:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    pairs = 0
    for count in anagram_dict.values():
        pairs += count * (count - 1) // 2
    return pairs >= 115