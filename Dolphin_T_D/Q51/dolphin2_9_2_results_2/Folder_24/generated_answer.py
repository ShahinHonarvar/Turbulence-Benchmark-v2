from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                counter1 = Counter(lst[i].lower())
                counter2 = Counter(lst[j].lower())
                if counter1 == counter2:
                    count += 1
                    if count >= 96:
                        return False
    return True if count >= 96 else False