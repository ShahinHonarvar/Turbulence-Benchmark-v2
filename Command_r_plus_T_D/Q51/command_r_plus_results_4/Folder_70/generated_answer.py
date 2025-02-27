def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) < 3:
            continue
        normalized_word = normalize_string(word)
        if normalized_word in anagram_dict:
            anagram_dict[normalized_word].append(word)
        else:
            anagram_dict[normalized_word] = [word]
    anagram_pairs = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 97