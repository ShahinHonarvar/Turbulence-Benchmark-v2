from collections import Counter

def if_contains_anagrams(lst):
    counter_dict = Counter()
    for word in lst:
        if len(word) >= 3:
            counter_dict[tuple(sorted(word.lower()))] += 1
    count = 0
    for value in counter_dict.values():
        count += (value - 1) // 2
    return count >= 67