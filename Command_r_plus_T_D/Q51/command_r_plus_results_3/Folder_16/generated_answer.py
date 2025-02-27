def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            word1 = words_list[i]
            word2 = words_list[j]
            if len(word1) < 3 or len(word2) < 3:
                continue
            normalized_word1 = normalize_text(word1)
            normalized_word2 = normalize_text(word2)
            sorted_word1 = sort_text(normalized_word1)
            sorted_word2 = sort_text(normalized_word2)
            if sorted_word1 == sorted_word2:
                anagram_pair = tuple(sorted([word1, word2]))
                if anagram_pair not in anagram_pairs:
                    anagram_pairs.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 24:
                        return False
    return True