def if_contains_anagrams(lst):
    cnt = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if sorted(lst[i].lower()) == sorted(lst[j].lower()):
                    cnt += 1
                if cnt > 48:
                    return False
    return cnt <= 48