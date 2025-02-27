def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)
    anagram_pairs = set()
    normalized_words = [normalize_text(word) for word in words_list]
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if is_anagram(normalized_words[i], normalized_words[j]) and len(normalized_words[i]) >= 3:
                anagram_pairs.add(tuple(sorted((normalized_words[i], normalized_words[j]))))
            if len(anagram_pairs) > 20:
                return False
    return True