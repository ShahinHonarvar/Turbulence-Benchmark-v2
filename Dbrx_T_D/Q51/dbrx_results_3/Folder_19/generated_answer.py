import collections

def if_contains_anagrams(lst):
    anagrams = collections.defaultdict(lambda: 0)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word] += 1
    return sum(anagrams.values()) <= 69