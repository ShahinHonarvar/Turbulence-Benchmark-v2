def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    normalized_words = [normalize_text(word) for word in words_list]
    sorted_words = [sort_text(word) for word in normalized_words]
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if sorted_words[i] == sorted_words[j] and len(words_list[i]) >= 3 and (len(words_list[j]) >= 3):
                anagram_pairs.add(frozenset({i, j}))
            if len(anagram_pairs) > 366:
                return False
    return True