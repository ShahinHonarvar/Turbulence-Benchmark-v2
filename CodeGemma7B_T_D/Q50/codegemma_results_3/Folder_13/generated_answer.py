def if_contains_anagrams(str_list):
    str_sort = sorted(str_list, key=len)
    result = []
    for i in range(len(str_sort)):
        for j in range(i + 1, len(str_sort)):
            if sorted(str_sort[i].lower()) == sorted(str_sort[j].lower()) and len(str_sort[i]) >= 3 and (len(str_sort[j]) >= 3):
                result.append(str_sort[i])
                result.append(str_sort[j])
    if len(result) >= 144:
        return True
    return False