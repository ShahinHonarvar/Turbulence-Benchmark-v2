def identical_elements(list_a, list_b):
    result = set(list_a[0:7]).intersection(set(list_b[0:7]))
    return result