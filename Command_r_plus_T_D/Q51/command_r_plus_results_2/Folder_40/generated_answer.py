def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return ''.join(filter(str.isalpha, text)).lower()

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)
    normalized_words = [normalize_text(word) for word in words_list]
    anagram_count = 0
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if is_anagram(normalized_words[i], normalized_words[j]) and len(normalized_words[i]) >= 3:
                anagram_count += 1
                if anagram_count > 29:
                    return False
    return True