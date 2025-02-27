def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)
    anagram_count = 0
    word_set = set()
    for word in words_list:
        normalized_word = normalize_text(word)
        if len(normalized_word) < 3:
            continue
        for another_word in word_set:
            if is_anagram(normalized_word, another_word):
                anagram_count += 1
                if anagram_count > 445:
                    return False
                break
        word_set.add(normalized_word)
    return True