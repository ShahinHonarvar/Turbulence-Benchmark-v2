def if_contains_anagrams(lst):
    count = 0
    seen = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            if len(str1) < 3 or len(str2) < 3:
                continue
            if sorted(str1) == sorted(str2) and str1 not in seen:
                seen.add(str1)
                count += 1
                if count == 366:
                    return True
    if count <= 366:
        return True
    else:
        return False