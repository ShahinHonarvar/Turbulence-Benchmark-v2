def if_contains_anagrams(words_list):

    def normalize_text(word):
        return word.lower()

    def sorted_word(word):
        return ''.join(sorted(normalize_text(word)))
    anagram_dict = {}
    for word in words_list:
        if len(word) >= 3:
            sorted_word_ = sorted_word(word)
            if sorted_word_ in anagram_dict:
                anagram_dict[sorted_word_].append(word)
            else:
                anagram_dict[sorted_word_] = [word]
    anagram_pairs_count = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs_count <= 11