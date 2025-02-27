def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)
    max_anagram_pairs = 188
    anagram_dict = {}
    anagram_count = 0
    for word in words_list:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word].append(word)
        else:
            anagram_dict[normalized_word] = [word]
    for anagram_group in anagram_dict.values():
        anagram_group_size = len(anagram_group)
        if anagram_group_size > 1:
            anagram_count += anagram_group_size * (anagram_group_size - 1) // 2
        if anagram_count > max_anagram_pairs:
            return False
    return True