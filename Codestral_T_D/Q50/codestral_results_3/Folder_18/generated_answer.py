from collections import defaultdict

def if_contains_anagrams(lst):
    groups = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            groups[''.join(sorted(word.lower()))].append(word)
    return any((len(group) >= 2 for group in groups.values()))