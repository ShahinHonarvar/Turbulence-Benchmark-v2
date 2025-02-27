def identical_elements(list_a, list_b):
    elements = set()
    for i in range(70, 85):
        if list_a[i] == list_b[i]:
            elements.add(list_a[i])
    return elements