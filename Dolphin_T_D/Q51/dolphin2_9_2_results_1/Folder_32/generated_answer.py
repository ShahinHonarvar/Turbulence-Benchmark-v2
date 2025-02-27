from collections import Counter
    from itertools import permutations

def if_contains_anagrams(lst):
    counter = Counter()
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                counter[lst[i]] += 1
    count = 0
    for key in counter:
        if counter[key] > 1:
            count += 1
    return count <= 44