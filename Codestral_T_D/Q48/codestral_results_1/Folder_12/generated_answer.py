def return_binary_or_hexa(num_tuple):
    a = num_tuple[16]
    b = num_tuple[87]
    missing_sum = sum((i for i in range(a + 1, b) if i not in num_tuple[16:87]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    else:
        return ''