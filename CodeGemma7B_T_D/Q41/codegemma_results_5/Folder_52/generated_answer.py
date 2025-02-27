def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        return set()
    identical_set = set()
    for i in range(28, 39):
        if list_a[i] == list_b[i]:
            identical_set.add(list_a[i])
    return identical_set