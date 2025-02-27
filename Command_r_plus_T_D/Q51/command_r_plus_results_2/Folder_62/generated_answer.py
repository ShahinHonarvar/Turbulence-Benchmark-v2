def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for i in range(len(lst)):
        normalized_str = normalize_string(lst[i])
        if len(normalized_str) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if normalized_str == normalize_string(lst[j]):
                anagram_pairs.add(frozenset({lst[i], lst[j]}))
            if len(anagram_pairs) > 289:
                return False
    return True