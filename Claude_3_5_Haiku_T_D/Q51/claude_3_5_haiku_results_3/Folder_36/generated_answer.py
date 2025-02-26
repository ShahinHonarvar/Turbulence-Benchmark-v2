def if_contains_anagrams(strings):

    def is_valid_string(s):
        return all((c.isalpha() for c in s))

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    valid_strings = [s for s in strings if is_valid_string(s) and len(s) >= 3]
    anagram_map = {}
    for s in valid_strings:
        normalized = normalize_string(s)
        if normalized not in anagram_map:
            anagram_map[normalized] = []
        anagram_map[normalized].append(s)
    anagram_count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_map.values() if len(group) > 1))
    return anagram_count <= 25