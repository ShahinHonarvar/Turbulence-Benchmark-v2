from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            anagrams[sorted_str].append(string)
    count = sum((len(group) * (len(group) - 1) // 2 for group in anagrams.values() if len(group) > 1))
    return count <= 289