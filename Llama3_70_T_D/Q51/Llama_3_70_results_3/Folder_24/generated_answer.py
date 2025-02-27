def if_contains_anagrams(lst):
    anagram_count = {}
    for string in lst:
        string_lower = string.lower()
        if len(string_lower) < 3:
            continue
        string_sorted = ''.join(sorted(string_lower))
        if string_sorted in anagram_count:
            anagram_count[string_sorted] += 1
        else:
            anagram_count[string_sorted] = 1
    pairs_count = sum(((count - 1) * count // 2 for count in anagram_count.values()))
    return pairs_count <= 96