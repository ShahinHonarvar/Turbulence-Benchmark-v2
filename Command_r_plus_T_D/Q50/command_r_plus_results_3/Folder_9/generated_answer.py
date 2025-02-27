def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(words_list)):
        normalized_word = normalize_string(words_list[i])
        if len(words_list[i]) < 3 or normalized_word in anagram_set:
            continue
        for j in range(i + 1, len(words_list)):
            if normalized_word == normalize_string(words_list[j]):
                anagram_set.add(normalized_word)
                anagram_count += 1
                if anagram_count >= 66:
                    return True
    return False