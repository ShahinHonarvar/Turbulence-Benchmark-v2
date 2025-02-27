def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    count = 0
    i = 0
    for j in range(i + 1, len(str_list)):
        while i < j and len(str_list[i]) < 3:
            i += 1
        if sorted(str_list[i]) == sorted(str_list[j]):
            count += 1
        i += 1
    if count >= 79:
        return True
    else:
        return False