def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            lst[i] = lst[i].lower()
            lst[j] = lst[j].lower()
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i]) == sorted(lst[j])):
                count += 1
    return count <= 79