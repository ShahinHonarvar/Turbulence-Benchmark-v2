def if_contains_anagrams(str_list):
    str_list = [str.lower() for str in str_list]
    str_list = [str for str in str_list if len(str) >= 3]
    str_list.sort(key=len)
    num_anagrams = 0
    for i in range(len(str_list) - 1):
        for j in range(i + 1, len(str_list)):
            if sorted(str_list[i]) == sorted(str_list[j]):
                num_anagrams += 1
                if num_anagrams >= 106:
                    return True
    return False