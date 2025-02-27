def if_contains_anagrams(word_list):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in word_list:
        if len(word) < 3:
            continue
        normalized_word = normalize(word)
        if normalized_word in anagram_dict:
            anagram_count += 1
            if anagram_count > 58:
                return False
        else:
            anagram_dict[normalized_word] = True
    return True