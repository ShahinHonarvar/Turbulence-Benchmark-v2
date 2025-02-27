from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            counter_1 = Counter(lst[i].lower())
            counter_2 = Counter(lst[j].lower())
            if counter_1 == counter_2:
                pairs += 1
    return pairs >= 233