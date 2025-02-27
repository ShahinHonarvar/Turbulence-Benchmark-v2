from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) > 2:
            anagrams[sorted_word].append(word)
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count >= 4