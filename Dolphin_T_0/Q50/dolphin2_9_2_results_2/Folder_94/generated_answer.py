from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            c = Counter(lst[i].lower())
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and Counter(lst[j].lower()) == c:
                    count += 1
    return count >= 46