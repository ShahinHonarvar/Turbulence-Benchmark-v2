def if_contains_anagrams(lst):
    count_ana = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    count_ana += 1
    if count_ana >= 55:
        return True
    else:
        return False