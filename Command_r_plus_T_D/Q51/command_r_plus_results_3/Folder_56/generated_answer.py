def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    normalized_strings = [normalize_string(s) for s in lst]
    anagram_pairs = set()
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j] and len(lst[i]) >= 3:
                anagram_pairs.add(tuple(sorted((i, j))))
    return len(anagram_pairs) <= 11