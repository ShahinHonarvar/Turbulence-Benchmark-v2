def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return text.lower()

    def is_anagram(str1: str, str2: str) -> bool:
        return sorted(str1) == sorted(str2)
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1, str2 = (normalize_text(lst[i]), normalize_text(lst[j]))
            if len(str1) >= 3 and len(str2) >= 3 and is_anagram(str1, str2):
                anagram_pairs.add(frozenset([str1, str2]))
            if len(anagram_pairs) > 423:
                return False
    return True