def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s))
    strings = [s.lower() for s in strings]
    anagram_map = {}
    for s in strings:
        if len(s) >= 3:
            key = sorted_str(s)
            if key in anagram_map:
                anagram_map[key] += 1
            else:
                anagram_map[key] = 1
    anagram_pairs = 0
    for count in anagram_map.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
            if anagram_pairs >= 9:
                return True
    return False