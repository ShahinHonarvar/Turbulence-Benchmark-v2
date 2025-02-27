def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list.sort(key=len)
    anagrams = []
    for str1 in str_list:
        for str2 in str_list:
            if str1 != str2 and sorted(str1) == sorted(str2):
                anagrams.append((str1, str2))
    return len(anagrams) <= 279