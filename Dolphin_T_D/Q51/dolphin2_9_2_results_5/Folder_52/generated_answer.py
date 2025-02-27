def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst_i = list(lst[i].lower())
                lst_j = list(lst[j].lower())
                lst_i.sort()
                lst_j.sort()
                if lst_i == lst_j:
                    count += 1
                    if count > 43:
                        return False
    return True