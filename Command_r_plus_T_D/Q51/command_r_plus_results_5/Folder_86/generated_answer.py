def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    normalized_words = set()
    for word in words_list:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in normalized_words:
            anagram_count += 1
        else:
            normalized_words.add(normalized_word)
    return anagram_count <= 48