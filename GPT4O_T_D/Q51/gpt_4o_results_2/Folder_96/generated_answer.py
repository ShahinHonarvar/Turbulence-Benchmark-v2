def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_str(s)
            if sorted_s in anagram_map:
                anagram_map[sorted_s].add(s.lower())
            else:
                anagram_map[sorted_s] = {s.lower()}
    anagram_pairs = 0
    for words in anagram_map.values():
        if len(words) > 1:
            anagram_pairs += len(words) - 1
            if anagram_pairs > 2:
                return False
    return True