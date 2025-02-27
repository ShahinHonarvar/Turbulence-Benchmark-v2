import re
import collections

def if_contains_anagrams(strings):
    anagrams = []
    for string in strings:
        sorted_string = ''.join(sorted(re.findall('\\b\\w{3,}\\b', string.lower())))
        anagram = tuple(collections.Counter(sorted_string))
        if anagram not in anagrams:
            anagrams.append(anagram)
    return len(anagrams) <= 92