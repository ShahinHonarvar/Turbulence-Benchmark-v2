def return_binary_or_hexa(num_tuple):
    a = num_tuple[56]
    b = num_tuple[90]
    missing_sum = sum((x for x in range(a + 1, b) if x not in num_tuple[56:91]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]