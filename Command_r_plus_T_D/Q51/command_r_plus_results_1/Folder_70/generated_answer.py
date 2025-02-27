def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    word_dict = {}
    for word in words_list:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in word_dict:
            anagram_pairs.add(tuple(sorted((word, word_dict[normalized_word]))))
        else:
            word_dict[normalized_word] = word
    return len(anagram_pairs) <= 97