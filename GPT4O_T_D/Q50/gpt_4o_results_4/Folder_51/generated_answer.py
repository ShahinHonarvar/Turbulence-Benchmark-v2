def if_contains_anagrams(strings):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            sorted_s = sorted_str(s)
            anagram_dict.setdefault(sorted_s, 0)
            anagram_dict[sorted_s] += 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 39