def identical_elements(list_1, list_2):
    set_1 = set(list_1[14:65])
    set_2 = set(list_2[14:65])
    return set_1.intersection(set_2)