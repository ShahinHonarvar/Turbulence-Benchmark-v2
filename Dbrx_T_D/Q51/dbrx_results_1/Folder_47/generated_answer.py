from collections import defaultdict

def group_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        anagrams[''.join(sorted(word.lower()))].append(word)
    return anagrams.values()

def count_anagram_pairs(words):
    anagrams = group_anagrams(words)
    return sum((len(group) > 1 for group in anagrams))

def if_contains_anagrams(words):
    return count_anagram_pairs(words) <= 366