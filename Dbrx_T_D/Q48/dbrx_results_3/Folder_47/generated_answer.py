def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[29], int_tuple[53])
    missing_sum = sum((x for x in range(a + 1, b) if x not in int_tuple[29:54]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()