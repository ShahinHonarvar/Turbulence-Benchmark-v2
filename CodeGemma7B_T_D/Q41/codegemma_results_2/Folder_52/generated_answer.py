def identical_elements(list_a, list_b):
    identical_set = set()
    for i in range(28, 39):
        if list_a[i] in list_b[i]:
            identical_set.add(list_a[i])
    return identical_set