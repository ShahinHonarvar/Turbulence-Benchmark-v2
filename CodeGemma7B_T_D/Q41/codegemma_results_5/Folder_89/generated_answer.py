def identical_elements(list_a, list_b):
    result_set = set()
    for i in range(56, 83):
        result_set.update({list_a[i], list_b[i]})
    return result_set