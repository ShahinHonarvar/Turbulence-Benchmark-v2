def if_contains_anagrams(words_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = {}
    for word in words_list:
        normalized_word = normalize_string(word)
        if len(word) < 3:
            continue
        if normalized_word in anagram_groups:
            anagram_groups[normalized_word].append(word)
        else:
            anagram_groups[normalized_word] = [word]
    anagram_pair_count = 0
    for group in anagram_groups.values():
        if len(group) > 1 and len(group) <= 3:
            anagram_pair_count += 1
    return anagram_pair_count <= 3