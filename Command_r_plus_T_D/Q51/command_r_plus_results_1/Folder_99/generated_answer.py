def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return ''.join(sorted(text.lower()))
    normalized_words = [normalize_text(word) for word in lst]
    anagram_pairs = [(i, j) for i in range(len(normalized_words)) for j in range(i + 1, len(normalized_words)) if normalized_words[i] == normalized_words[j]]
    anagram_count = len(anagram_pairs)
    return anagram_count <= 93