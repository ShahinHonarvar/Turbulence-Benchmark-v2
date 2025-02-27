from collections import defaultdict 

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            anagrams[''.join(sorted(word.lower()))].append(word)
    pairs = sum((len(words) * (len(words) - 1) // 2 for words in anagrams.values() if len(words) > 1))
    return pairs <= 28