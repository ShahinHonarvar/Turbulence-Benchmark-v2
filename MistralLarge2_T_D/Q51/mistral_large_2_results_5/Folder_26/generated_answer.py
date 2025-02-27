from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagram_count = 0
    anagram_map = defaultdict(list)
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagram_map[sorted_string].append(string)
    for key in anagram_map:
        if len(anagram_map[key]) > 1:
            anagram_count += len(anagram_map[key]) * (len(anagram_map[key]) - 1) // 2
    return anagram_count <= 35