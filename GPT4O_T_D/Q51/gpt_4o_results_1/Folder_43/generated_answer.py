def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_map = {}
    for s in strings:
        if len(s) < 3:
            continue
        normalized = normalize(s)
        if normalized in anagram_map:
            anagram_map[normalized].add(s.lower())
        else:
            anagram_map[normalized] = {s.lower()}
    pairs = 0
    for value in anagram_map.values():
        count = len(value)
        if count > 1:
            pairs += count * (count - 1) // 2
            if pairs > 3:
                return False
    return True