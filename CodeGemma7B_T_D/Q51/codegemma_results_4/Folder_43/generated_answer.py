def if_contains_anagrams(str_list):
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            str1 = str_list[i].lower()
            str2 = str_list[j].lower()
            if len(str1) != len(str2):
                break
            sorted_str1 = sorted(str1)
            sorted_str2 = sorted(str2)
            if sorted_str1 == sorted_str2:
                count_pairs += 1
    if count_pairs <= 3:
        return True
    else:
        return False