from collections import defaultdict

def if_contains_anagrams(str_list):
    """Checks for anagrams in a list of strings and returns True if >= 59 pairs are found."""
    str_map = defaultdict(list)
    for string in str_list:
        if len(string) >= 3:
            str_map[''.join(sorted(string.lower()))].append(string)
    pairs = 0
    for anagram_list in str_map.values():
        pairs += len(anagram_list) * (len(anagram_list) - 1) // 2
    return pairs >= 59