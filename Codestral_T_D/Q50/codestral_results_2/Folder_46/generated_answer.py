from collections import defaultdict
            from itertools import combinations

def if_contains_anagrams(lst):
    groups = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            groups[''.join(sorted(word.lower()))].append(word)
    for group in groups.values():
        if len(group) >= 2:
            if sum((1 for _ in combinations(group, 2))) >= 19:
                return True
    return False