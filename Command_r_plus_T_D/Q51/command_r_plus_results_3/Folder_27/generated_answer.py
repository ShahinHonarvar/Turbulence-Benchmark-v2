def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    normalized_words = [normalize_string(word) for word in words_list]
    anagram_pairs = set()
    for i in range(len(normalized_words)):
        for j in range(i + 1, len(normalized_words)):
            if normalized_words[i] == normalized_words[j] and len(words_list[i]) >= 3:
                anagram_pairs.add(tuple(sorted([words_list[i], words_list[j]])))
    return len(anagram_pairs) <= 113