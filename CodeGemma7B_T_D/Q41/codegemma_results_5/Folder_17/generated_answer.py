def identical_elements(list_a, list_b):
    result = set()
    for i in range(62, 79):
        if list_a[i] in list_b[i]:
            result.add(list_a[i])
    return result