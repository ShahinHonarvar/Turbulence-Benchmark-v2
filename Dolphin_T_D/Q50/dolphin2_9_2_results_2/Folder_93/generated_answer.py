def if_contains_anagrams(lst):
    n = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    n += 1
    if n >= 18:
        return True
    else:
        return False