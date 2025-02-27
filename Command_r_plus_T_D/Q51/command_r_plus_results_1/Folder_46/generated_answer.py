def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    anagram_dict = {}
    for word in words_list:
        normalized_word = normalize_text(word)
        sorted_word = sort_text(normalized_word)
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = [normalized_word]
        else:
            anagram_dict[sorted_word].append(normalized_word)
    anagram_count = 0
    for anagram_group in anagram_dict.values():
        if len(anagram_group) > 1 and len(anagram_group[0]) >= 3:
            anagram_count += 1
    return anagram_count <= 61