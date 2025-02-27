def if_contains_anagrams(lst):
    count = 0
    i = 0
    while i < len(lst):
        j = i + 1
        while j < len(lst):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    count += 1
                    lst.pop(j)
                    break
                j += 1
            else:
                j += 1
        i += 1
    return count <= 6