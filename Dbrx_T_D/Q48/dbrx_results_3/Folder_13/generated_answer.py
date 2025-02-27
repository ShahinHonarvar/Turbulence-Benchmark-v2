def return_binary_or_hexa(integer_tuple):
    a = integer_tuple[46]
    b = integer_tuple[91]
    sum_not_present = sum((i for i in range(a + 1, b) if i not in integer_tuple[46:92]))
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()