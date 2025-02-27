def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    words_set = set(words_list)
    for word1 in words_set:
        for word2 in words_set:
            if word1 != word2 and is_anagram(normalize_text(word1), normalize_text(word2)) and (len(word1) >= 3):
                anagram_count += 1
                if anagram_count > 70:
                    return False
    return True