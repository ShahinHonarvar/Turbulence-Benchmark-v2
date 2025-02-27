from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagram_map[sorted_string].append(string)
    for group in anagram_map.values():
        if len(group) > 1:
            anagram_count += len(group) - 1
    return anagram_count <= 116