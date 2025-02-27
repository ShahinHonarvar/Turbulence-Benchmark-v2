def if_contains_anagrams(word_list: list[str]) -> bool:

    def is_anagram(str1: str, str2: str) -> bool:
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                if is_anagram(word_list[i], word_list[j]):
                    anagram_count += 1
                    if anagram_count >= 50:
                        return True
    return False