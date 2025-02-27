def if_contains_anagrams(words_list):

    def normalize_text(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_text(word)
        if len(word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word].append(word)
        else:
            anagram_dict[normalized_word] = [word]
    anagram_pairs = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 43