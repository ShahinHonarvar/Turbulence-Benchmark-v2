def identical_elements(list_one, list_two):
    set_one = {item for item in list_one[35:50]}
    set_two = {item for item in list_two[35:50]}
    return set_one & set_two