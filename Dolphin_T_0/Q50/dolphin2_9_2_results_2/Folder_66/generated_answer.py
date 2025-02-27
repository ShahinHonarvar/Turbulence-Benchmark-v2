def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            lst[i] = ''.join(sorted(lst[i].lower()))
            lst[j] = ''.join(sorted(lst[j].lower()))
            if len(lst[i]) >= 3 and lst[i] == lst[j]:
                count += 1
            if count >= 92:
                return True
    return False