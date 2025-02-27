def identical_elements(list_a, list_b):
    result = set()
    for i in range(25, 88):
        if list_a[i] == list_b[i]:
            result.add(list_a[i])
    return result