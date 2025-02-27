from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    count = 0
    for anagram_group in anagrams.values():
        if len(anagram_group) > 1:
            count += len(anagram_group) * (len(anagram_group) - 1) // 2
    return count <= 61