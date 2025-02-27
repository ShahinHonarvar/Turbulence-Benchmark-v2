def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_string(s: str) -> str:
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_str = normalize_string(lst[i])
        if len(normalized_str) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if normalized_str == normalize_string(lst[j]):
                anagram_pair = tuple(sorted((lst[i], lst[j])))
                if anagram_pair not in anagram_set:
                    anagram_set.add(anagram_pair)
                    anagram_count += 1
                    if anagram_count > 49:
                        return False
    return True