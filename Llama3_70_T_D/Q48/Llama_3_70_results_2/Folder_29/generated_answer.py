def return_binary_or_hexa(num_tuple):
    a = num_tuple[70]
    b = num_tuple[98]
    full_range = set(range(a + 1, b))
    tuple_range = set(num_tuple[70:99])
    missing_nums = full_range - tuple_range
    total = sum(missing_nums)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]