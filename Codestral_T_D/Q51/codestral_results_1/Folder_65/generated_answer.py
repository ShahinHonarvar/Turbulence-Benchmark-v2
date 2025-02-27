from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    return sum((len(anagram_list) * (len(anagram_list) - 1) / 2 for anagram_list in anagrams.values())) <= 72