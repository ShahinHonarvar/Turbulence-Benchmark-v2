def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return s.lower()

    def is_anagram(s1: str, s2: str) -> bool:
        return sorted(s1) == sorted(s2)
    anagram_count = 0
    word_set = set(map(normalize_string, words_list))
    for word in word_set:
        if len(word) < 3:
            continue
        for another_word in word_set:
            if word == another_word:
                continue
            if is_anagram(word, another_word):
                anagram_count += 1
                if anagram_count >= 8:
                    return True
    return False