from collections import Counter

def if_contains_anagrams(lst):
    n = len(lst)
    pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (Counter(lst[i].lower()) == Counter(lst[j].lower())):
                pairs += 1
    return pairs <= 49