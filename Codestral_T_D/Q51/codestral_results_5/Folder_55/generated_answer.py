def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        normalized_string = ''.join(sorted(string.lower())).replace(' ', '')
        if len(normalized_string) >= 3:
            if normalized_string not in anagram_groups:
                anagram_groups[normalized_string] = 1
            else:
                anagram_groups[normalized_string] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_groups.values()))
    return anagram_pairs <= 44