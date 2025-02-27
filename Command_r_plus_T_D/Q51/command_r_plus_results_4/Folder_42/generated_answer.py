def if_contains_anagrams(str_list: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
    anagram_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3:
                normalized_str1 = normalize_text(str_list[i])
                normalized_str2 = normalize_text(str_list[j])
                if is_anagram(normalized_str1, normalized_str2):
                    anagram_count += 1
                    if anagram_count > 38:
                        return False
    return True