def identical_elements(list_a, list_b):
    set_a = set(list_a[91:99 + 1])
    set_b = set(list_b[91:99 + 1])
    result = set_a.intersection(set_b)
    return result or set()