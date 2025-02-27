def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError('The two lists must have the same length')
    result = set()
    for i in range(200, len(list_a)):
        if list_a[i] in list_b[i]:
            result.add(list_a[i])
    return result