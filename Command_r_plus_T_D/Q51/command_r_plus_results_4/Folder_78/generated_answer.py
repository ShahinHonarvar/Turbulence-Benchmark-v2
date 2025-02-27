def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return ''.join(filter(str.isalpha, text)).lower()
    anagram_count = 0
    normalized_strings = [normalize_text(s) for s in lst]
    for i in range(len(normalized_strings)):
        for j in range(i + 1, len(normalized_strings)):
            if normalized_strings[i] == normalized_strings[j] and len(normalized_strings[i]) >= 3:
                anagram_count += 1
                if anagram_count > 70:
                    return False
    return True