def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)
    anagram_pairs = 0
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                normalized_word1 = normalize_text(words_list[i])
                normalized_word2 = normalize_text(words_list[j])
                if is_anagram(normalized_word1, normalized_word2):
                    anagram_pairs += 1
                    if anagram_pairs >= 7:
                        return True
    return False