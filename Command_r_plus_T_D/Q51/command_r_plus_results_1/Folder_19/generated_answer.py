def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        normalized_word = normalize_string(word)
        if len(word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word] += 1
        else:
            anagram_dict[normalized_word] = 1
    anagram_count = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_count <= 69