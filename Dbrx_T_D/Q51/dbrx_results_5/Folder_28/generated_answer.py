from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagrams = defaultdict(list)
    for string in string_list:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for anagram_keys in anagrams.values():
        anagram_count += len(anagram_keys) - 1
        if anagram_count > 78:
            return False
    return anagram_count <= 78