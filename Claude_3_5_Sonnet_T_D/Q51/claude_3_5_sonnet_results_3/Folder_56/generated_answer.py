from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_groups = defaultdict(list)
    for s in string_list:
        cleaned_s = ''.join((char.lower() for char in s if char.isalpha()))
        if len(cleaned_s) >= 3:
            sorted_s = ''.join(sorted(cleaned_s))
            anagram_groups[sorted_s].append(s)
    for group in anagram_groups.values():
        if len(group) > 1:
            anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 11