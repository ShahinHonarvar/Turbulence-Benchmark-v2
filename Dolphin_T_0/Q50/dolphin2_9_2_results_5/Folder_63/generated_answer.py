def if_contains_anagrams(lst):
    counter = 0
    for i in range(len(lst)):
        if len(lst[i]) < 3:
            continue
        for j in range(i + 1, len(lst)):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                counter += 1
    return counter >= 89