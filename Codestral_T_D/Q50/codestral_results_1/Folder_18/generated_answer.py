from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_groups = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_groups[sorted_string].append(string)
    for group in anagram_groups.values():
        if len(group) >= 2:
            if len(group) * (len(group) - 1) / 2 >= 10 ** 6:
                return True
    return False