def identical_elements(list_a, list_b):
    identical_set = set()
    for i in range(26, 53):
        if list_a[i] == list_b[i]:
            identical_set.add(list_a[i])
    return identical_set