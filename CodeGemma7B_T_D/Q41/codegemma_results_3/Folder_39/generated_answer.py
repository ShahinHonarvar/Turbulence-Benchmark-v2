def identical_elements(a, b):
    element_set = set()
    for i in range(20, 31):
        if a[i] == b[i]:
            element_set.add(a[i])
    return element_set