def return_binary_or_hexa(input_tuple):
    a = input_tuple[17]
    b = input_tuple[88]
    missing_sum = sum((i for i in range(a + 1, b) if i not in input_tuple[17:88]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()