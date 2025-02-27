def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    anagrams = []
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i]
            str2 = str_list[j]
            if len(str1) >= 3 and len(str2) >= 3 and (str1 != str2) and (sorted(str1) == sorted(str2)):
                anagrams.append((str1, str2))
    return len(anagrams) >= 35