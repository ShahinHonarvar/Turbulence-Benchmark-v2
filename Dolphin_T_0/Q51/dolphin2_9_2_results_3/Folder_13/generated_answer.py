def if_contains_anagrams(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                sorted_i = sorted(lst[i].lower())
                sorted_j = sorted(lst[j].lower())
                if sorted_i == sorted_j:
                    counter += 1
        if counter > 54:
            return False
    return counter