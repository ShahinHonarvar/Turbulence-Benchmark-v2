from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            if counter[tuple(sorted(word.lower()))] in [0, 2]:
                counter[tuple(sorted(word.lower()))] += 1
    return all((value == 2 for value in counter.values())) if len(counter.values()) <= 255 else False