def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_string(word)
        if len(word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word] += 1
        else:
            anagram_dict[normalized_word] = 1
    anagram_pairs = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_pairs <= 18