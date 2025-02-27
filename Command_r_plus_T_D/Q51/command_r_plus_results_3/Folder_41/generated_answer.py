def if_contains_anagrams(words_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_map = {}
    for word in words_list:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in anagram_map:
            anagram_map[normalized_word].append(word)
        else:
            anagram_map[normalized_word] = [word]
    for anagram_group in anagram_map.values():
        if len(anagram_group) > 1 and len(anagram_group) <= 52:
            anagram_count += 1
    return anagram_count <= 52