def return_binary_or_hexa(num_tuple):
    a = num_tuple[42]
    b = num_tuple[87]
    full_set = set(range(a + 1, b))
    tuple_set = set(num_tuple[42:88])
    diff_set = full_set - tuple_set
    total_sum = sum(diff_set)
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]