from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for c in range(len(lst)):
        for d in range(c + 1, len(lst)):
            if len(lst[c]) >= 3 and len(lst[d]) >= 3 and (Counter(lst[c].lower()) == Counter(lst[d].lower())):
                count += 1
    return count >= 3