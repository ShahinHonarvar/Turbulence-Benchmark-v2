def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join(sorted(text.lower()))
    anagram_pairs = set()
    for i in range(len(lst)):
        normalized_i = normalize_text(lst[i])
        if len(normalized_i) < 3:
            continue
        for j in range(i + 1, len(lst)):
            normalized_j = normalize_text(lst[j])
            if normalized_i == normalized_j:
                anagram_pairs.add(frozenset({i, j}))
                if len(anagram_pairs) > 81:
                    return False
    return True