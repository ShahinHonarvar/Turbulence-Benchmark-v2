from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    anagrams_counter = Counter(''.join((sorted(s.lower()) for s in lst if len(s) >= 3)))
    for count in anagrams_counter.values():
        if count > 257:
            return False
    return True