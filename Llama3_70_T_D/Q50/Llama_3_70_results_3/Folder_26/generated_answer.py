def if_contains_anagrams(lst):
    anagram_count = {}
    for string in lst:
        lower_str = string.lower()
        sorted_str = ''.join(sorted(lower_str))
        if len(lower_str) >= 3:
            if sorted_str in anagram_count:
                anagram_count[sorted_str] += 1
            else:
                anagram_count[sorted_str] = 1
    anagram_pairs = 0
    for count in anagram_count.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 49