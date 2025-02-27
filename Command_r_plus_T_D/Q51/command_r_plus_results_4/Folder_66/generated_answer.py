def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    words_normalized = set()
    for word in words_list:
        if len(word) >= 3 and word.isalpha():
            normalized_word = normalize_string(word)
            if normalized_word in words_normalized:
                anagram_pairs.add(frozenset({word, words_normalized[normalized_word]}))
            words_normalized.add(normalized_word)
    return len(anagram_pairs) <= 64