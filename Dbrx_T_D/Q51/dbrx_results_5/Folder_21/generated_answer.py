from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        anagrams[sorted_string].append(string)
    for value in anagrams.values():
        if len(value) > 26:
            return False
    return True