def if_contains_anagrams(words_list):

    def normalize_text(word):
        return ''.join(filter(str.isalpha, word)).lower()
    anagram_count = 0
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        sorted_word = ''.join(sorted(normalized_word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(normalized_word)
        else:
            anagram_dict[sorted_word] = [normalized_word]
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1:
            anagram_count += 1
    return anagram_count <= 67