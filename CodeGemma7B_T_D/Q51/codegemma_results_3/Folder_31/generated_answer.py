from collections import Counter

def if_contains_anagrams(str_lst):
    str_lst = [Counter(s.lower()) for s in str_lst if len(s) >= 3]
    count = 0
    for i in range(len(str_lst)):
        for j in range(i + 1, len(str_lst)):
            if str_lst[i] == str_lst[j]:
                count += 1
    return count <= 65