from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_count = 0
    anagrams = defaultdict(lambda: defaultdict(int))
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        anagrams[sorted_string][string] += 1
    for value in anagrams.values():
        anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count <= 46