def identical_elements(list_1, list_2):
    set_1 = set(list_1)
    set_2 = set(list_2)
    common_elements = set_1 & set_2
    return common_elements