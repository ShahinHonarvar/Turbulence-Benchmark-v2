def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list.sort(key=len)
    i = 0
    j = 1
    while j < len(str_list):
        if sorted(str_list[i]) == sorted(str_list[j]):
            if len(str_list[i]) >= 3:
                count += 1
        i += 1
        j += 1
    return count >= 6