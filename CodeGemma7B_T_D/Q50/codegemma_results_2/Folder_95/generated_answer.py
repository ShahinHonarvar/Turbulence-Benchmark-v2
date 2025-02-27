def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list.sort(key=len)
    pairs = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i]
            str2 = str_list[j]
            list1 = list(str1)
            list2 = list(str2)
            list1.sort()
            list2.sort()
            if len(str1) >= 3 and list1 == list2:
                pairs += 1
    return pairs >= 93