def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                lst[i] = lst[i].lower()
                lst[j] = lst[j].lower()
                if sorted(lst[i]) == sorted(lst[j]):
                    count += 1
                    if count >= 3:
                        return True
    return False