from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (Counter(lst[i].lower() + lst[j].lower()) == Counter(lst[j].lower() + lst[i].lower())):
                count += 1
                if count >= 464:
                    return True
    return False