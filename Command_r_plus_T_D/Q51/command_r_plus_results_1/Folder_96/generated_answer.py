def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    normalized_strings = [normalize_string(s) for s in lst]
    anagram_pairs = set()
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j] and len(normalized_strings[i]) >= 3:
                anagram_pairs.add(frozenset({i, j}))
            if len(anagram_pairs) > 2:
                return False
    return True