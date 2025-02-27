def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_string(word)
        if len(word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word].append(word)
        else:
            anagram_dict[normalized_word] = [word]
    anagram_pairs = [pair for pair in anagram_dict.values() if len(pair) > 1]
    return len(anagram_pairs) <= 6