def if_contains_anagrams(lst):
    count = 0
    l = len(lst)
    for i in range(l):
        for j in range(i + 1, l):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    count += 1
                    if count >= 97:
                        return True
    return False