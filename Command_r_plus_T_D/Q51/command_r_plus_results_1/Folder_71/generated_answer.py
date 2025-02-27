def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word_i, word_j = (words_list[i], words_list[j])
            if len(word_i) >= 3 and len(word_j) >= 3:
                normalized_i, normalized_j = map(normalize_text, [word_i, word_j])
                sorted_i, sorted_j = map(sort_text, [normalized_i, normalized_j])
                if sorted_i == sorted_j:
                    anagram_pairs.add(frozenset([word_i, word_j]))
            if len(anagram_pairs) > 9:
                return False
    return True