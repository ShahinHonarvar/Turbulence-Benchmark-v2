def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                str1 = sorted(lst[i].lower())
                str2 = sorted(lst[j].lower())
                if str1 == str2:
                    count += 1
    return count <= 72