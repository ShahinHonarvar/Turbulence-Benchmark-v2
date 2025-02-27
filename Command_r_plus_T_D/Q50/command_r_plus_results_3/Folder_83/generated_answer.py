def if_contains_anagrams(word_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(word_list)):
        normalized_word = normalize_string(word_list[i])
        if len(normalized_word) < 3:
            continue
        for j in range(i + 1, len(word_list)):
            if normalized_word == normalize_string(word_list[j]):
                anagram_pair = tuple(sorted((word_list[i], word_list[j])))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count >= 48:
                        return True
    return False