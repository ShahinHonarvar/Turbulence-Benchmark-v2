def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    for i in range(len(lst)):
        normalized_str = normalize(lst[i])
        if len(normalized_str) >= 3:
            for j in range(i + 1, len(lst)):
                if normalized_str == normalize(lst[j]):
                    anagram_pairs.add(frozenset({lst[i], lst[j]}))
    return len(anagram_pairs) <= 47