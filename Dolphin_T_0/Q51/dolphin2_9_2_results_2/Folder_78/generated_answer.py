from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                c1 = Counter(lst[i].lower())
                c2 = Counter(lst[j].lower())
                if c1 == c2:
                    count += 1
                if count >= 70:
                    return True
    return count <= 70