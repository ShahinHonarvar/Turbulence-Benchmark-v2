from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_map = defaultdict(list)
    for string in str_list:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(string)
        else:
            anagram_map[sorted_str] = [string]
    for anagram_list in anagram_map.values():
        if len(anagram_list) >= 178:
            return True
    return False