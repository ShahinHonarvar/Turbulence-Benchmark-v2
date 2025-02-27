from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] += 1
    for key in counter:
        if counter[key] > 1:
            if counter[key] > 2:
                return True
    return False