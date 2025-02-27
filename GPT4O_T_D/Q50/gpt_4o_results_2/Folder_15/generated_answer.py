def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = sorted_string(string)
        if sorted_str in anagram_map:
            anagram_map[sorted_str] += 1
        else:
            anagram_map[sorted_str] = 1
    for occurrences in anagram_map.values():
        if occurrences > 1:
            count += occurrences * (occurrences - 1) // 2
    return count >= 4