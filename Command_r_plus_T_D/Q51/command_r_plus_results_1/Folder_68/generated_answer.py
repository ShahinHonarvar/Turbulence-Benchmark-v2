def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            normalized_str1 = normalize_text(lst[i])
            normalized_str2 = normalize_text(lst[j])
            if is_anagram(normalized_str1, normalized_str2) and len(normalized_str1) >= 3:
                anagram_pairs.add(frozenset([normalized_str1, normalized_str2]))
            if len(anagram_pairs) > 94:
                return False
    return True