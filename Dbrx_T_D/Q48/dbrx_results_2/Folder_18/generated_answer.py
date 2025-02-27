def return_binary_or_hexa(int_tuple):
    a = int_tuple[56]
    b = int_tuple[90]
    present_set = set(int_tuple[57:90])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_set))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()