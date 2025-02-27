def return_binary_or_hexa(int_tuple):
    a, b = (int_tuple[20], int_tuple[200])
    missing_sum = sum((i for i in range(a + 1, b) if i not in int_tuple[20:201]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()