from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_pairs = 0
    if not isinstance(string_list, list) or len(string_list) < 2:
        return False
    anagram_map = defaultdict(set)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        anagram_map[sorted_string].add(string)
    for value in anagram_map.values():
        if len(value) > 1:
            anagram_pairs += 1
            if anagram_pairs > 173:
                return True
    return False