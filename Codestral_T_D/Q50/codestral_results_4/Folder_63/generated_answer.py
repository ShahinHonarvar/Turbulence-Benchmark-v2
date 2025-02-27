from collections import defaultdict

def if_contains_anagrams(str_list):
    groups = defaultdict(list)
    for word in str_list:
        if len(word) >= 3:
            groups[''.join(sorted(word.lower()))].append(word)
    return sum((len(group) * (len(group) - 1) // 2 for group in groups.values())) >= 89