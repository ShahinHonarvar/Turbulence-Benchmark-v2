from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    count = 0
    for group in anagrams.values():
        if len(group) >= 2:
            count += len(group) * (len(group) - 1) // 2
    return count <= 11