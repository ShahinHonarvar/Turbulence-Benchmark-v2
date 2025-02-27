def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                normalized_i = normalize_text(lst[i])
                normalized_j = normalize_text(lst[j])
                if is_anagram(normalized_i, normalized_j):
                    anagram_pairs.add(frozenset({lst[i], lst[j]}))
            if len(anagram_pairs) > 131:
                return False
    return True