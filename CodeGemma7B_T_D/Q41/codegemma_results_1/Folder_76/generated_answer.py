def identical_elements(list_a, list_b):
    low = 686
    high = 987
    set_a = set(list_a[low:high + 1])
    set_b = set(list_b[low:high + 1])
    return set_a & set_b