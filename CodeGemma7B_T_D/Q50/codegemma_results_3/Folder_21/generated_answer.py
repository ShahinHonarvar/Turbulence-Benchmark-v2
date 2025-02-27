from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in lst:
        for j in lst:
            if i != j and Counter(i.lower()) == Counter(j.lower()) and (len(i) >= 3) and (len(j) >= 3):
                count += 1
    return count >= 136