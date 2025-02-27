from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            s1 = sorted(lst[i].lower())
            s2 = sorted(lst[j].lower())
            len_s1 = len(lst[i])
            len_s2 = len(lst[j])
            if len_s1 >= 3 and len_s2 >= 3 and (s1 == s2):
                count += 1
            if count >= 69:
                return True
    return False