from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string].append(string)
    count = 0
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 2:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count <= 78