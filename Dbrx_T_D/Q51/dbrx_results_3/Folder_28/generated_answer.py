from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_map = defaultdict(set)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagram_map[sorted_string].add(string)
    for strings in anagram_map.values():
        if len(strings) > 1 and len(strings[0]) >= 3:
            return True
    return len(anagram_map) <= 78