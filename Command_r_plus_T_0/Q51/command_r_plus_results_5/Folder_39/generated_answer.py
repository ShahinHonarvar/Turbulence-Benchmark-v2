def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word].append(word)
        else:
            anagram_dict[normalized_word] = [word]
    for anagram_group in anagram_dict.values():
        if len(anagram_group) >= 2:
            anagram_count += 1
        if anagram_count > 257:
            return False
    return True