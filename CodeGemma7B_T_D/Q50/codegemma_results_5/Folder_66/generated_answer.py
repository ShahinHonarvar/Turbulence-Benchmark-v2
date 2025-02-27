def if_contains_anagrams(str_list):
    str_set = set((str.lower() for str in str_list if len(str) >= 3))
    count = 0
    for str1 in str_set:
        for str2 in str_set:
            if str1 != str2 and sorted(str1) == sorted(str2):
                count += 1
                if count >= 92:
                    return True
    return False