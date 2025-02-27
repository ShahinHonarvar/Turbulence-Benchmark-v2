from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        key = ''.join(sorted(word.lower()))
        if len(key) < 3:
            continue
        anagrams[key].append(word)
    for group in anagrams.values():
        if len(group) >= 46:
            return True
    return False