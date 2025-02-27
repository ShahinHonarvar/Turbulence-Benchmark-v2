def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(string: str) -> str:
        return ''.join(string.lower())
    anagram_count = 0
    anagram_dict = {}
    for word in words_list:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in anagram_dict:
            anagram_count += 1
            if anagram_count >= 52:
                return True
        else:
            anagram_dict[normalized_word] = word
    return False