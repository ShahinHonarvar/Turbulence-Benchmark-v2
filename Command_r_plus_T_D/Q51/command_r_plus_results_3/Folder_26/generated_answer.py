def if_contains_anagrams(words):

    def normalize_word(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = set()
    word_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized_word = normalize_word(word)
        if normalized_word in word_dict:
            anagram_pairs.add(frozenset({word, word_dict[normalized_word]}))
        else:
            word_dict[normalized_word] = word
    return len(anagram_pairs) <= 35