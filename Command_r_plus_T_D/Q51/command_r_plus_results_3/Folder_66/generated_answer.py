def if_contains_anagrams(lst: list[str]) -> bool:

    def normalize_text(text: str) -> str:
        return ''.join(sorted(text.lower()))
    anagram_count = 0
    anagram_set = set()
    for i in range(len(lst)):
        normalized_i = normalize_text(lst[i])
        if len(normalized_i) < 3:
            continue
        for j in range(i + 1, len(lst)):
            normalized_j = normalize_text(lst[j])
            if len(normalized_j) < 3:
                continue
            if normalized_i == normalized_j:
                pair = tuple(sorted((lst[i], lst[j])))
                if pair not in anagram_set:
                    anagram_set.add(pair)
                    anagram_count += 1
                    if anagram_count > 64:
                        return False
    return True