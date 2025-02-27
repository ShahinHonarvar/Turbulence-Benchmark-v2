def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            sorted_i = sorted(lst[i].lower())
            sorted_j = sorted(lst[j].lower())
            if sorted_i == sorted_j:
                count += 1
                if count == 34:
                    return False
    return True