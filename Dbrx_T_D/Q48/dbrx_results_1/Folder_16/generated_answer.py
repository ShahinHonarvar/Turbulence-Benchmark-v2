def return_binary_or_hexa(int_tuple):
    a = int_tuple[90]
    b = int_tuple[97]
    missing_sum = sum((x for x in range(a + 1, b) if x not in int_tuple[90:98]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()