def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sorted_text(text: str) -> str:
        return ''.join(sorted(text))
    normalized_words = [normalize_text(word) for word in words_list]
    anagram_count = 0
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if len(normalized_words[i]) >= 3 and len(normalized_words[j]) >= 3:
                if sorted_text(normalized_words[i]) == sorted_text(normalized_words[j]):
                    anagram_count += 1
                    if anagram_count > 181:
                        return False
    return True