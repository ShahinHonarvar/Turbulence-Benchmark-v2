def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        normalized_word = normalize_string(word)
        if len(word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_count += 1
            if anagram_count > 28:
                return False
        else:
            anagram_dict[normalized_word] = word
    return True