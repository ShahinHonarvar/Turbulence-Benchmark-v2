def if_contains_anagrams(lst):
    count = 0
    for i in range(1, len(lst)):
        for j in range(i):
            if sorted(lst[i].lower()) == sorted(lst[j].lower()) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                count += 1
    return count >= 153