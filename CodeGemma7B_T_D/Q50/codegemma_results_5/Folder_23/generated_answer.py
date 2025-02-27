def if_contains_anagrams(str_list):
    str_list_sorted = sorted(str_list, key=len)
    num_anagrams = 0
    for i in range(len(str_list_sorted)):
        for j in range(i + 1, len(str_list_sorted)):
            if len(str_list_sorted[i]) >= 3 and len(str_list_sorted[j]) >= 3:
                if sorted(str_list_sorted[i].lower()) == sorted(str_list_sorted[j].lower()):
                    num_anagrams += 1
    return num_anagrams >= 67