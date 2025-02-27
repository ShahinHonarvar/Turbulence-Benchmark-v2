def if_contains_anagrams(strings):
    anagram_counts = {}
    for string in strings:
        if len(string) >= 3:
            normalized_string = ''.join(sorted(string.lower()))
            anagram_counts[normalized_string] = anagram_counts.get(normalized_string, 0) + 1
    pair_count = sum([count * (count - 1) // 2 for count in anagram_counts.values()])
    return pair_count <= 255