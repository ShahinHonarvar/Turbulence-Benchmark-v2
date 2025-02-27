from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) > 2 and len(lst[j]) > 2 and (Counter(lst[i].lower()) == Counter(lst[j].lower())):
                pairs += 1
    return pairs <= 67