def identical_elements(first_list, second_list):
    set1 = set(first_list[0:8])
    set2 = set(second_list[0:8])
    return set1 & set2