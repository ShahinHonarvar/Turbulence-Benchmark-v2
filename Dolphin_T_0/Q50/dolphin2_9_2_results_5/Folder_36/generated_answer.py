def if_contains_anagrams(str_list):
    result = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if len(str_list[i]) >= 3 and len(str_list[j]) >= 3 and (sorted(str_list[i].lower()) == sorted(str_list[j].lower())):
                result += 1
    return result >= 312