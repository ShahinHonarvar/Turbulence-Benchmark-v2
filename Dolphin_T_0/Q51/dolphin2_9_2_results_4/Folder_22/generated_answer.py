from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3 and lst[i].lower() != lst[i].upper():
            for j in range(i + 1, len(lst)):
                if Counter(lst[i].lower()) == Counter(lst[j].lower()) and lst[j].lower() != lst[j].upper():
                    count += 1
                    if count >= 14:
                        return False
    if count <= 14:
        return True