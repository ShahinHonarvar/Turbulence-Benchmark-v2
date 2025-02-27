from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            counter[sorted_word] += 1
    return any((v >= 2 for v in counter.values()))