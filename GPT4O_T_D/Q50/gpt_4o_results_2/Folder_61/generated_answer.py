def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        normalized = normalize(s)
        if len(s) >= 3:
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    for count in anagram_dict.values():
        if count > 1:
            anagram_count += count * (count - 1) // 2
            if anagram_count >= 8:
                return True
    return False