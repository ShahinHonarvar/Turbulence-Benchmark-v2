def return_binary_or_hexa(int_tuple):
    a = int_tuple[70]
    b = int_tuple[98]
    sum_not_present = sum((i for i in range(a + 1, b) if i not in int_tuple[70:99]))
    if sum_not_present % 2:
        return bin(sum_not_present)[2:]
    else:
        return hex(sum_not_present)[2:].upper()