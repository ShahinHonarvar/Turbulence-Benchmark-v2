from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    anagram_count = 0
    anagrams = defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for anagram in anagrams.values():
        if len(anagram) >= 2:
            anagram_count += len(anagram) * (len(anagram) - 1) // 2
    return anagram_count >= 246