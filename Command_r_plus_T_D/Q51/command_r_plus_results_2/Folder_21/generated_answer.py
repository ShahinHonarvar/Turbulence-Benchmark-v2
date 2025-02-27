def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        normalized = normalize_string(word)
        if len(word) < 3:
            continue
        if normalized in anagram_dict:
            anagram_dict[normalized] += 1
        else:
            anagram_dict[normalized] = 1
    pair_count = sum((1 for count in anagram_dict.values() if count == 2))
    return pair_count <= 26