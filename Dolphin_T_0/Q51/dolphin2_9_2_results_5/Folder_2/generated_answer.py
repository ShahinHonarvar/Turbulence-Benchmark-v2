from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for string in lst:
        if len(string) >= 3:
            count[tuple(sorted(string.lower()))] += 1
    return any((value > 1 for value in count.values()))