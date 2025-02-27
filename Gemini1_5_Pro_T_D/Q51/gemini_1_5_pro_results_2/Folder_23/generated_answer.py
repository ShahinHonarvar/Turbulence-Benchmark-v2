from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_groups = defaultdict(list)
    for string in list_of_strings:
        if len(string) >= 3:
            anagram_groups[''.join(sorted(string.lower()))].append(string)
    count = 0
    for key in anagram_groups:
        n = len(anagram_groups[key])
        if n >= 2:
            count += n * (n - 1) // 2
    if count <= 49:
        return True
    else:
        return False