from collections import defaultdict

def if_contains_anagrams(string_list):
    groups = defaultdict(list)
    for s in string_list:
        if len(s) >= 3:
            groups[''.join(sorted(s.lower()))].append(s)
    return sum((len(g) * (len(g) - 1) // 2 for g in groups.values())) >= 39