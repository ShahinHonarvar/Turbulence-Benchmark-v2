def if_contains_anagrams(strings):

    def sorted_chars(s):
        return ''.join(sorted([c.lower() for c in s if c.isalpha()]))
    anagram_map = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_chars(s)
            if sorted_s in anagram_map:
                anagram_map[sorted_s] += 1
            else:
                anagram_map[sorted_s] = 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return pairs_count <= 44