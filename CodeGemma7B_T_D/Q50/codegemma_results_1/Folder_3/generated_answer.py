from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for string in str_list:
        normalized_str = ''.join(sorted(string.lower()))
        if len(normalized_str) >= 3:
            anagrams[normalized_str].append(string)
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 30:
            return True
    return False