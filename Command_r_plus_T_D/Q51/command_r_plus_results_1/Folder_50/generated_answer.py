def if_contains_anagrams(words_list):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in words_list:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in anagram_dict:
            anagram_count += 1
            if anagram_count > 47:
                return False
        else:
            anagram_dict[normalized_word] = word
    return True