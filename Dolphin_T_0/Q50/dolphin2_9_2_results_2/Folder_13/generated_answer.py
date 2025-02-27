def if_contains_anagrams(lst):
    res = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    res += 1
    if res >= 144:
        return True
    else:
        return False