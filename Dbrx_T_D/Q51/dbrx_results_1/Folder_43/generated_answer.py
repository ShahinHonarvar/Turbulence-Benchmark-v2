import re

def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        sorted_s = ''.join(sorted(re.findall('[a-zA-Z]{3,}', s.lower())))
        if sorted_s:
            anagrams.append(sorted_s)
    anagram_set = set(anagrams)
    return len(anagram_set) - len(anagrams) <= 3