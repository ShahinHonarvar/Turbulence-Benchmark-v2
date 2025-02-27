from collections import defaultdict

def if_contains_anagrams(string_list):
    anagram_count = 0
    anagrams = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for anagram in anagrams.values():
        if len(anagram) >= 3 and len(anagram) > 1:
            anagram_count += len(anagram) - 1
            if anagram_count > 52:
                return False
    return True