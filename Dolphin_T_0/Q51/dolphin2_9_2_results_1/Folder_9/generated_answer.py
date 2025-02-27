def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower(), key=lambda c: (c.lower(), c)) == sorted(lst[j].lower(), key=lambda c: (c.lower(), c)):
                    count += 1
    if count <= 475:
        return True
    else:
        return False