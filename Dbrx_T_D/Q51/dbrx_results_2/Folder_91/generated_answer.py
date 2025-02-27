from collections import Counter

def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagrams:
            return True
        anagrams.add(sorted_string)
    return len(anagrams) > 88