def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort(key=len)
    i = 0
    count = 0
    while i < len(str_list) - 1:
        j = i + 1
        while j < len(str_list) and len(str_list[i]) == len(str_list[j]):
            if sorted(str_list[i]) == sorted(str_list[j]):
                count += 1
                if count > 279:
                    return False
            j += 1
        i += 1
    return True