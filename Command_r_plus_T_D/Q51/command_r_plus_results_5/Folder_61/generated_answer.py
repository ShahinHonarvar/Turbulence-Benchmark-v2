def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    word_norm_map = {}
    for word in words_list:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in word_norm_map:
            anagram_pairs.add(frozenset({word, word_norm_map[normalized_word]}))
        else:
            word_norm_map[normalized_word] = word
    return len(anagram_pairs) <= 50