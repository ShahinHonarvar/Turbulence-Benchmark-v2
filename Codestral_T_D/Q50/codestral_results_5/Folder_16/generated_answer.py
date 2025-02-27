from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_groups = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagram_groups[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = sum([len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()])
    return anagram_pairs >= 155