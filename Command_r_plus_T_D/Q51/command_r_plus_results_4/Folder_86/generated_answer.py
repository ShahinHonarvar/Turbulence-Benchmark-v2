def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        normalized_word_i = normalize_text(words_list[i])
        sorted_word_i = sort_text(normalized_word_i)
        for j in range(i + 1, len(words_list)):
            normalized_word_j = normalize_text(words_list[j])
            sorted_word_j = sort_text(normalized_word_j)
            if len(normalized_word_i) >= 3 and len(normalized_word_j) >= 3:
                if sorted_word_i == sorted_word_j:
                    anagram_count += 1
                    anagram_pair = tuple(sorted([words_list[i], words_list[j]]))
                    anagram_pairs.add(anagram_pair)
                    if anagram_count > 48:
                        return False
    return True