def identical_elements(in_list_a, in_list_b):
    in_set = set()
    for i in range(5, 8):
        if in_list_a[i] in in_list_b[i]:
            in_set.add(in_list_a[i])
    return in_set