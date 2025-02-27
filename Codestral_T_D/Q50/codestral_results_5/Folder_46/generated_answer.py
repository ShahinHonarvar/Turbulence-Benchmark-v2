from collections import defaultdict

def if_contains_anagrams(lst):
    groups = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            groups[sorted_word].append(word)
    return sum((len(group) * (len(group) - 1) // 2 for group in groups.values())) >= 38