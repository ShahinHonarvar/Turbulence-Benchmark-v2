def if_contains_anagrams(lst):
    anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst1 = sorted(lst[i].lower())
                lst2 = sorted(lst[j].lower())
                if lst1 == lst2:
                    anagrams += 1
    return anagrams >= 34