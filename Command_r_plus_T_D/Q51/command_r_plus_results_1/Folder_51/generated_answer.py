def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(words_list)):
        normalized_word = normalize_text(words_list[i])
        sorted_word = sort_text(normalized_word)
        if len(normalized_word) < 3:
            continue
        for j in range(i + 1, len(words_list)):
            another_normalized_word = normalize_text(words_list[j])
            another_sorted_word = sort_text(another_normalized_word)
            if len(another_normalized_word) < 3:
                continue
            if sorted_word == another_sorted_word:
                anagram_tuple = (normalized_word, another_normalized_word)
                if anagram_tuple not in anagram_set:
                    anagram_set.add(anagram_tuple)
                    anagram_count += 1
            if anagram_count > 116:
                return False
    return True