def identical_elements(list_a, list_b):
    set_list_a = set(list_a[23:24])
    set_list_b = set(list_b[23:24])
    same_elements = set_list_a & set_list_b
    if not same_elements:
        return set()
    return same_elements