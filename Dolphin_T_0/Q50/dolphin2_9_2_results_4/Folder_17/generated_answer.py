from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for word in lst:
        if len(word) >= 3:
            count.update(Counter(word.lower()))
    return any((value >= 2 for value in count.values()))