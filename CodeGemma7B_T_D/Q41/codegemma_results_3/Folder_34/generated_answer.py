def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError('Lists must have the same length')
    result = set()
    for i in range(60, 201):
        if list_a[i] == list_b[i]:
            result.add(list_a[i])
    return result