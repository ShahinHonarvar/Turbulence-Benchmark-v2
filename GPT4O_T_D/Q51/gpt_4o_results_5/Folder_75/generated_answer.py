from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        prepared_string = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(prepared_string) >= 3:
            anagram_groups[prepared_string].append(string)
    anagram_count = 0
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 55