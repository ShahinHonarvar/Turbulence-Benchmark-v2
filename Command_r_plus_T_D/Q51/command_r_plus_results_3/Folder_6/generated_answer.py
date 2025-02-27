def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return ''.join(sorted(text.lower()))
    anagram_count = 0
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized_word = normalize_text(word)
        if normalized_word in anagram_dict:
            anagram_count += 1
            anagram_dict[normalized_word] += 1
        else:
            anagram_dict[normalized_word] = 1
    return anagram_count <= 86