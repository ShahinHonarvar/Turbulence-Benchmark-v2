def if_contains_anagrams(str_list):
    if len(str_list) <= 464:
        return True
    str_list = [str.lower() for str in str_list]
    str_list.sort(key=len)
    i, j = (0, 1)
    pairs = 0
    while j < len(str_list):
        if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3 and (str_list[i] != str_list[j]):
            pairs += 1
            i = j
            j += 1
        else:
            j += 1
    if pairs <= 464:
        return True
    else:
        return False