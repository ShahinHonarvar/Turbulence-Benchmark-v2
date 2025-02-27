def if_contains_anagrams(lst):
    count = 0
    letters = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            str1 = lst[i].lower()
            str2 = lst[j].lower()
            if set(str1) == set(str2) and str1 != str2:
                count += 1
                if count > 147:
                    return False
    return count > 147