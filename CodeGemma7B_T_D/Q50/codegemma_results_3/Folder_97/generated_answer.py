def if_contains_anagrams(str_list):
    str_length = len(str_list)
    num_of_anagrams = 0
    for i in range(str_length):
        for j in range(i + 1, str_length):
            str_1 = str_list[i]
            str_2 = str_list[j]
            if len(str_1) >= 3 and len(str_2) >= 3 and (str_1.lower() == str_2.lower()):
                num_of_anagrams += 1
    if num_of_anagrams >= 123:
        return True
    return False