def if_contains_anagrams(lst):
    result = False
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    if not result:
                        result = True
                    if lst.count(lst[i]) > 1:
                        lst.remove(lst[i])
                        lst.remove(lst[j])
                        j -= 1
            if j == len(lst) and (not result):
                return result
    return result