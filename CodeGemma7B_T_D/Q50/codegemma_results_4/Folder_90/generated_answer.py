def if_contains_anagrams(str_list):
    str_list = [x.lower() for x in str_list]
    str_list = sorted(str_list, key=len)
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            list1 = list(str_list[i])
            list2 = list(str_list[j])
            list1.sort()
            list2.sort()
            if list1 == list2 and len(str_list[i]) >= 3 and (len(str_list[j]) >= 3):
                anagrams.append((str_list[i], str_list[j]))
    if len(anagrams) >= 177:
        return True
    else:
        return False