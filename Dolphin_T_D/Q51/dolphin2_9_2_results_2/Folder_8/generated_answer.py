from collections import Counter
    from itertools import permutations

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for word in list_of_strings:
        if len(word) >= 3:
            word = word.lower()
            counter.update(tuple(sorted(word)))
    count = 0
    for val in counter.values():
        if val % 2 == 1:
            count += 1
    return count <= 68