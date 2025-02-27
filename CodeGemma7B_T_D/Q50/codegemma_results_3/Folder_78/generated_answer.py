def if_contains_anagrams(str_list):
    str_list = [str(x).lower() for x in str_list]
    str_list.sort()
    result = False
    count = 0
    for j in range(len(str_list)):
        for k in range(j + 1, len(str_list)):
            if sorted(str_list[j]) == sorted(str_list[k]) and len(str_list[j]) >= 3:
                count += 1
    if count >= 79:
        result = True
    return result