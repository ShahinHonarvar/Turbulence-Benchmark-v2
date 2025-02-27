def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst1 = sorted(lst[i].lower())
                lst2 = sorted(lst[j].lower())
                if lst1 == lst2:
                    count += 1
                    if count >= 41:
                        return False
    return True if count <= 41 else False