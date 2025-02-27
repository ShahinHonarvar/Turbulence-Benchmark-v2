def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    normalized_strings = {}
    for s in strings:
        if len(s) >= 3:
            norm_s = normalize(s)
            if norm_s in normalized_strings:
                anagram_count += normalized_strings[norm_s]
                normalized_strings[norm_s] += 1
            else:
                normalized_strings[norm_s] = 1
    return anagram_count >= 96