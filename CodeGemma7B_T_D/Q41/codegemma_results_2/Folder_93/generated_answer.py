def identical_elements(list_a, list_b):
    same_elements = set()
    for index in range(75, 95):
        if list_a[index] == list_b[index]:
            same_elements.add(list_a[index])
    return same_elements