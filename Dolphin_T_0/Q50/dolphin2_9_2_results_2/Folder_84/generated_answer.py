def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i].lower()) >= 3 and len(lst[j].lower()) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    count += 1
    if count >= 108:
        return True
    else:
        return False