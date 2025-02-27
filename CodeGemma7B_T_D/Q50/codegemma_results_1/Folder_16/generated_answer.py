def if_contains_anagrams(str_list):
    str_list = sorted(str_list, key=len)
    anagrams = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            if sorted(str1) == sorted(str2) and len(str1) >= 3:
                anagrams += 1
    return anagrams >= 155