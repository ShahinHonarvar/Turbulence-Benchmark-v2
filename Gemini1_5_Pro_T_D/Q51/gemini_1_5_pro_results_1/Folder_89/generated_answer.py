from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagram_groups[''.join(sorted(string.lower()))].append(string)
    count = 0
    for group in anagram_groups.values():
        count += len(group) * (len(group) - 1) // 2
        if count > 73:
            return False
    return True