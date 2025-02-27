def return_binary_or_hexa(req_tuple):
    a, b = (req_tuple[0], req_tuple[8])
    valid_sum = sum(set(range(a + 1, b)) - set(req_tuple[1:8]))
    if valid_sum % 2:
        return format(valid_sum, '08b')
    else:
        return format(valid_sum, '02x').upper()