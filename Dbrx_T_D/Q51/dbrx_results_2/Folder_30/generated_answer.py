from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    count = 0
    for anagram in anagrams.values():
        if len(anagram) > 1:
            count += 1
            if count > 28:
                return False
    return True