import rereto
from collections import defaultdict

def if_contains_anagrams(strings_list):
    anagrams = defaultdict(list)
    count = 0
    for s in strings_list:
        anagrams[''.join(sorted(reterto.split(s.lower())))].append(s)
    for anagram in anagrams.values():
        if len(anagram) >= 2:
            count += len(anagram) * (len(anagram) - 1) // 2
            if count >= 155:
                return True
    return False