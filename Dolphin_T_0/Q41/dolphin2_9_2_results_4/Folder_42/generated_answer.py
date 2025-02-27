def identical_elements(list_1, list_2):
    set_1 = set(list_1[29:80])
    set_2 = set(list_2[29:80])
    return set_1.intersection(set_2)