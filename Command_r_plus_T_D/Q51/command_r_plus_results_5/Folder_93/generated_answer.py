def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sorted_chars(text: str) -> str:
        return ''.join(sorted(text))
    normalized_words = [normalize_text(word) for word in words_list]
    anagram_count = {}
    for word in normalized_words:
        sorted_word = sorted_chars(word)
        if sorted_word not in anagram_count:
            anagram_count[sorted_word] = 1
        else:
            anagram_count[sorted_word] += 1
    anagram_pairs = sum((1 for count in anagram_count.values() if count > 1))
    return anagram_pairs <= 36