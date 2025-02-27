def return_binary_or_hexa(input_tuple):
    a = input_tuple[77]
    b = input_tuple[84]
    missing_sum = sum(set(range(a + 1, b)) - set(input_tuple[77:85]))
    if missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:].upper()