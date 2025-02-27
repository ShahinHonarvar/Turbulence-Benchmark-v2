def if_contains_anagrams(str_list):
    str_list1 = [s.lower() for s in str_list if len(s) >= 3 and s.isalpha()]
    str_list1.sort(key=len)
    count = 0
    for i in range(len(str_list1)):
        for j in range(i + 1, len(str_list1)):
            if sorted(str_list1[i]) == sorted(str_list1[j]):
                count += 1
    if count <= 75:
        return True
    else:
        return False