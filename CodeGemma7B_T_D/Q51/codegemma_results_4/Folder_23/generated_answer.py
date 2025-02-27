def if_contains_anagrams(str_list):
    str_list_sort = sorted(str_list, key=len)
    anagrams_count = 0
    for i in range(len(str_list_sort) - 1):
        for j in range(i + 1, len(str_list_sort)):
            if sorted(str_list_sort[i].lower()) == sorted(str_list_sort[j].lower()):
                anagrams_count += 1
    if anagrams_count <= 49:
        return True
    else:
        return False