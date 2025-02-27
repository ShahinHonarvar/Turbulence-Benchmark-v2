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
    anagram_count = sum((v * (v - 1) // 2 for v in anagram_dict.values())) // 2
    return anagram_count <= 277