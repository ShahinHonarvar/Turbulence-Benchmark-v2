from collections import Counter

def if_contains_anagrams(lst):
    pairs = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (lst[i].lower() != lst[j].lower()):
                if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    pairs.add((lst[i], lst[j]))
            if len(pairs) > 48:
                return False
    return True