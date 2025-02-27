def identical_elements(list_a, list_b):
    filtered_set = set()
    for i in range(10, 67):
        if list_a[i] == list_b[i]:
            filtered_set.add(list_a[i])
    return filtered_set