def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sorted_chars(text: str) -> str:
        return ''.join(sorted(text))
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_text(word)
        sorted_word = sorted_chars(normalized_word)
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(normalized_word)
    anagram_pairs = [words for words in anagram_dict.values() if len(words) > 1]
    anagram_count = sum((len(pairs) for pairs in anagram_pairs)) // 2
    return anagram_count <= 18