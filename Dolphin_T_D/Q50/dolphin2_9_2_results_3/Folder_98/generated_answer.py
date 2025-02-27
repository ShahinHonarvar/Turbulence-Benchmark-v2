from collections import Counter

def if_contains_anagrams(lst):
    counter_lst = Counter()
    for word in lst:
        if len(word) >= 3:
            counter_lst[tuple(sorted(word.lower()))] += 1
    count = 0
    for val in counter_lst.values():
        if val >= 2:
            count += 1
    return count > 6