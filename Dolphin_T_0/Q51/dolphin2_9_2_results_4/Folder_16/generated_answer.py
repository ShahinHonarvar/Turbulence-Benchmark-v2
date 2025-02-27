from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for word in list_of_strings:
        counter[tuple(sorted(word.lower()))] += 1
    return any((value > 2 for value in counter.values()))