from collections import defaultdict

def if_contains_anagrams(strings):
    anagram_dict = defaultdict(list)
    for s in strings:
        if len(s) >= 3:
            anagram_dict[''.join(sorted(s.lower()))].append(s)
    for key in anagram_dict:
        if len(anagram_dict[key]) >= 2:
            return True
    return False