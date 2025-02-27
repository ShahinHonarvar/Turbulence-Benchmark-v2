def if_contains_anagrams(word_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(word1: str, word2: str) -> bool:
        return sorted(word1) == sorted(word2)
    count = 0
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            if len(word_list[i]) >= 3 and len(word_list[j]) >= 3:
                if is_anagram(normalize_text(word_list[i]), normalize_text(word_list[j])):
                    count += 1
                    if count >= 22:
                        return True
    return False