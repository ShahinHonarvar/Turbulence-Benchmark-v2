def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            normalized = normalize_string(word)
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    anagram_pairs = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_pairs <= 52