def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list = sorted(str_list, key=len)
    i = 0
    count = 0
    while i < len(str_list) - 1:
        j = i
        while j < len(str_list):
            temp = str_list[j]
            str_list[j] = str_list[i]
            str_list[i] = temp
            if str_list[j] == str_list[i] and len(str_list[i]) >= 3:
                count += 1
            j += 1
        i += 1
    if count >= 43:
        return True
    else:
        return False