from collections import Counter

def if_contains_anagrams(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            lst_i = ''.join(sorted(lst[i].lower()))
            lst_j = ''.join(sorted(lst[j].lower()))
            if len(lst_i) >= 3 and len(lst_j) >= 3 and (Counter(lst_i) == Counter(lst_j)):
                cnt += 1
    return cnt // 2 <= 407