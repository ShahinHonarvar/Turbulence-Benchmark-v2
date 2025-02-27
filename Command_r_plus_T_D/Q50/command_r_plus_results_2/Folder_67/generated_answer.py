def if_contains_anagrams(words_list: list[str]) -> bool:

    def normalize_string(string: str) -> str:
        return ''.join(sorted(string.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(words_list)):
        normalized_word = normalize_string(words_list[i])
        if len(words_list[i]) < 3:
            continue
        for j in range(i + 1, len(words_list)):
            if normalized_word == normalize_string(words_list[j]):
                anagram_pair = tuple(sorted((words_list[i], words_list[j])))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count >= 41:
                        return True
    return False