def if_contains_anagrams(strings):

    def sorted_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = {}
    for string in strings:
        if len(string) >= 3:
            sorted_str = sorted_string(string)
            if sorted_str in anagram_groups:
                anagram_groups[sorted_str].add(string.lower())
            else:
                anagram_groups[sorted_str] = {string.lower()}
    anagram_pairs = 0
    for group in anagram_groups.values():
        size = len(group)
        if size > 1:
            anagram_pairs += size * (size - 1) // 2
    return anagram_pairs <= 52