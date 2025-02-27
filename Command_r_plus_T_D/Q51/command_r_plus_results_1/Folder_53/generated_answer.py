def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                normalized_i = normalize(lst[i])
                normalized_j = normalize(lst[j])
                if normalized_i == normalized_j:
                    anagram_pairs.add((i, j))
                    if len(anagram_pairs) > 8:
                        return False
    return True