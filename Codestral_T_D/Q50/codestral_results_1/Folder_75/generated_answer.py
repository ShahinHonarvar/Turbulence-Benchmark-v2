from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    checked = set()
    for i in range(len(lst)):
        if lst[i] in checked:
            continue
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            if Counter(lst[i].lower()) == Counter(lst[j].lower()):
                count += 1
                if count >= 70:
                    return True
        checked.add(lst[i])
    return False