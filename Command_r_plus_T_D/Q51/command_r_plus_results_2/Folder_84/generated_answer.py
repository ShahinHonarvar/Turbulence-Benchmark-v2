def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sorted_text(text: str) -> str:
        return ''.join(sorted(normalize_text(text)))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = sorted_text(word)
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_pairs = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 16