def if_contains_anagrams(lst):
    counter = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) < 3 or len(lst[j]) < 3:
                continue
            lst[i] = lst[i].lower()
            lst[j] = lst[j].lower()
            if sorted(lst[i]) == sorted(lst[j]):
                counter += 1
    return counter >= 79