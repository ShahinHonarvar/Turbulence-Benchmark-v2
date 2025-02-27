def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if len(words_list[i]) >= 3 and len(words_list[j]) >= 3:
                normalized_i = normalize_string(words_list[i])
                normalized_j = normalize_string(words_list[j])
                if normalized_i == normalized_j and (words_list[i], words_list[j]) not in anagram_pairs:
                    anagram_count += 1
                    anagram_pairs.add((words_list[i], words_list[j]))
                    if anagram_count > 5:
                        return False
    return True