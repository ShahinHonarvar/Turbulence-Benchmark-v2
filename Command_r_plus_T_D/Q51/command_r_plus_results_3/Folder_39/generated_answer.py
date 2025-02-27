def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()
    anagram_count = 0
    anagram_set = set()
    for word1 in words_list:
        normalized_word1 = normalize_text(word1)
        for word2 in words_list:
            normalized_word2 = normalize_text(word2)
            if normalized_word1 != normalized_word2 and sorted(normalized_word1) == sorted(normalized_word2) and (len(normalized_word1) >= 3):
                anagram_pair = tuple(sorted([normalized_word1, normalized_word2]))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 257:
                        return False
    return True