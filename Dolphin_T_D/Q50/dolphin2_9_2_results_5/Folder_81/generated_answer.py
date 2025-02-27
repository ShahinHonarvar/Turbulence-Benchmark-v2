from collections import Counter

def if_contains_anagrams(lst):
    counter = Counter()
    for word in lst:
        if len(word) >= 3:
            counter[tuple(sorted(word.lower()))] = counter.get(tuple(sorted(word.lower())), 0) + 1
        if len(counter) >= 16:
            return True
    return False