def if_contains_anagrams(words_list: list[str]) -> bool:

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1.lower()) == sorted(word2.lower())
    anagram_count = 0
    for i in range(len(words_list)):
        for j in range(i + 1, len(words_list)):
            if is_anagram(words_list[i], words_list[j]) and len(words_list[i]) >= 3:
                anagram_count += 1
                if anagram_count >= 19:
                    return True
    return False