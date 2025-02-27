def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_string(string)
            if sorted_str in anagram_map:
                anagram_map[sorted_str] += 1
            else:
                anagram_map[sorted_str] = 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 233