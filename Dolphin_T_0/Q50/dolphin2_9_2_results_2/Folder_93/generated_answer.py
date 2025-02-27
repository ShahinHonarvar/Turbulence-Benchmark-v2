def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and len(lst[i].lower()) >= 3 and (len(lst[j].lower()) >= 3) and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                count += 1
                if count >= 18:
                    return True
    return False