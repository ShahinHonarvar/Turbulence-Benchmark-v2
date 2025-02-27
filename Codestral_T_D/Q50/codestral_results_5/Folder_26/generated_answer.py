from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    anagram_count = sum([len(group) * (len(group) - 1) // 2 for group in anagrams.values()])
    return anagram_count >= 49