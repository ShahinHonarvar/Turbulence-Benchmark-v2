from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagrams[key].append(word)
    counter = 0
    for values in anagrams.values():
        if len(values) > 1:
            counter += len(values) - 1
        if counter >= 6:
            return True
    return False