def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagrams_set = set()
    for i in range(len(words_list)):
        normalized_word = normalize_string(words_list[i])
        if len(words_list[i]) >= 3 and normalized_word not in anagrams_set:
            for j in range(i + 1, len(words_list)):
                if normalized_word == normalize_string(words_list[j]):
                    anagram_count += 1
                    anagrams_set.add(normalized_word)
                    if anagram_count >= 277:
                        return True
    return False