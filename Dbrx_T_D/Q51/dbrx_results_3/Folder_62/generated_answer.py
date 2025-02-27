from collections import defaultdict

def if_contains_anagrams(string_list):
    if len(string_list) > 289:
        return False
    anagrams = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        anagrams[sorted_string].append(string)
    for group in anagrams.values():
        if len(group) >= 3:
            return True
    return False