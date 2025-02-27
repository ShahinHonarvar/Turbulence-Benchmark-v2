def if_contains_anagrams(lst):
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                sorted_i = sorted(lst[i].lower())
                sorted_j = sorted(lst[j].lower())
                if sorted_i == sorted_j:
                    anagram_pairs.add(frozenset([lst[i], lst[j]]))
    anagram_count = len(anagram_pairs)
    return anagram_count >= 26