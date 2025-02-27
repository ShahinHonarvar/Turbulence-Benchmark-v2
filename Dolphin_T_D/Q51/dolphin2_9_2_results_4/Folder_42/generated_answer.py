def if_contains_anagrams(lst):
    count = 0
    length = len(lst)
    for i in range(length):
        for j in range(i + 1, length):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst[i] = lst[i].lower()
                lst[j] = lst[j].lower()
                if sorted(lst[i]) == sorted(lst[j]):
                    count += 1
                    if count > 38:
                        return False
    return True