def if_contains_anagrams(list_of_strings):
    anagram_count = {}
    for s in list_of_strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            anagram_count[sorted_str] = anagram_count.get(sorted_str, 0) + 1
    pairs = sum((n * (n - 1) // 2 for n in anagram_count.values()))
    return pairs <= 81