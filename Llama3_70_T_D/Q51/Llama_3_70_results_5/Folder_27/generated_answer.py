import collections

def if_contains_anagrams(lst):
    anagrams = collections.defaultdict(list)
    for word in lst:
        clean_word = ''.join((e for e in word.lower() if e.isalpha()))
        if len(clean_word) >= 3:
            anagrams[''.join(sorted(clean_word))].append(clean_word)
    pairs = sum((1 for v in anagrams.values() if len(v) > 1))
    return pairs <= 113