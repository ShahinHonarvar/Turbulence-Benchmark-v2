def if_contains_anagrams(str_lst):
    count = 0
    for i in range(len(str_lst)):
        for j in range(i + 1, len(str_lst)):
            if sorted(str_lst[i].lower()) == sorted(str_lst[j].lower()) and len(str_lst[i]) >= 3 and (len(str_lst[j]) >= 3):
                count += 1
    if count >= 38:
        return True
    else:
        return False