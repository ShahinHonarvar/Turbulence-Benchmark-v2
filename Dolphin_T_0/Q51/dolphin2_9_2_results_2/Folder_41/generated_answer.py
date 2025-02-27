from collections import Counter

def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(word) >= 3 and key in anagrams:
            anagrams[key] += 1
        elif len(word) >= 3:
            anagrams[key] = 1
    for count in anagrams.values():
        if count > 2:
            return True
    return False