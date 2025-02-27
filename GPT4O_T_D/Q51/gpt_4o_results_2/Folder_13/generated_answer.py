from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_groups[sorted_string].append(string)
    count = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return count <= 54