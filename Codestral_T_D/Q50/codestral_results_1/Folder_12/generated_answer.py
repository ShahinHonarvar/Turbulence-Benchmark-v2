def if_contains_anagrams(strings):
    anagram_groups = {}
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagram_groups:
                anagram_groups[sorted_string].append(string)
            else:
                anagram_groups[sorted_string] = [string]
    anagram_pairs = 0
    for group in anagram_groups.values():
        if len(group) >= 2:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 69