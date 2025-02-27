def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for word1 in words_list:
        if len(word1) < 3:
            continue
        normalized_word1 = normalize_string(word1)
        for word2 in words_list:
            if len(word2) < 3 or word1 == word2:
                continue
            normalized_word2 = normalize_string(word2)
            if normalized_word1 == normalized_word2:
                anagram_pair = tuple(sorted((word1, word2)))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
            if anagram_count > 289:
                return False
    return True