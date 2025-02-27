def if_contains_anagrams(str_list):
    str_list = [s.lower() for s in str_list]
    str_list.sort()
    count = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]) and len(str_list[i]) >= 3 and (len(str_list[j]) >= 3):
                count += 1
            if count >= 277:
                return True
    return False