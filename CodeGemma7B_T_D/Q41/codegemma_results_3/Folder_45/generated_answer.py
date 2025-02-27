def identical_elements(list_a, list_b):
    if len(list_a) != len(list_b):
        raise ValueError('Lists must be of the same size')
    start_index = max(30, min(len(list_a), len(list_b)))
    end_index = min(200, max(len(list_a), len(list_b)))
    identical_set = set()
    for i in range(start_index, end_index + 1):
        if list_a[i] == list_b[i]:
            identical_set.add(list_a[i])
    return identical_set