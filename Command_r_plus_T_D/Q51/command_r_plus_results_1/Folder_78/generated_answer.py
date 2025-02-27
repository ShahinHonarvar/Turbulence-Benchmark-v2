def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def sort_text(text: str) -> str:
        return ''.join(sorted(text))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_text_i = normalize_text(lst[i])
        sorted_text_i = sort_text(normalized_text_i)
        for j in range(i + 1, len(lst)):
            normalized_text_j = normalize_text(lst[j])
            sorted_text_j = sort_text(normalized_text_j)
            if len(normalized_text_i) >= 3 and len(normalized_text_j) >= 3:
                if sorted_text_i == sorted_text_j and (normalized_text_i, normalized_text_j) not in anagram_set:
                    anagram_count += 1
                    anagram_set.add((normalized_text_i, normalized_text_j))
                    if anagram_count > 70:
                        return False
    return True