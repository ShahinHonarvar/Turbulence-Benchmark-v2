from collections import defaultdict

def if_contains_anagrams(strings: list) -> bool:
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for anagram_list in anagrams.values():
        if len(anagram_list) > 77:
            return False
    for anagram_list in anagrams.values():
        if len(anagram_list) >= 3:
            return True
    return False