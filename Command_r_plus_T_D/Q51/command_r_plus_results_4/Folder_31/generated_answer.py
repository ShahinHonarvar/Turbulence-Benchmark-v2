def if_contains_anagrams(words_list):

    def normalize_text(text):
        return text.lower()

    def sort_text(text):
        return ''.join(sorted(text))
    anagram_pairs = set()
    words_set = set(words_list)
    for word in words_set:
        normalized_word = normalize_text(word)
        sorted_word = sort_text(normalized_word)
        for existing_word in words_set:
            if existing_word == word:
                continue
            if sort_text(normalize_text(existing_word)) == sorted_word:
                anagram_pairs.add(frozenset({word, existing_word}))
                if len(anagram_pairs) > 65:
                    return False
    return True