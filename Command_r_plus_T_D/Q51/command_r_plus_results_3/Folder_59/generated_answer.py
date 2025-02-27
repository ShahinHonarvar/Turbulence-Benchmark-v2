def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_text(word)
        sorted_word = sort_text(normalized_word)
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(normalized_word)
        else:
            anagram_dict[sorted_word] = [normalized_word]
    anagram_pairs = [pair for pair in anagram_dict.values() if len(pair) > 1]
    anagram_pairs_count = sum((1 for pair in anagram_pairs if len(pair) >= 3))
    return anagram_pairs_count <= 15