def return_binary_or_hexa(int_tuple):
    non_present_sum = 0
    a, b = (int_tuple[46], int_tuple[91])
    for num in range(a + 1, b):
        if num not in int_tuple[46:92]:
            non_present_sum += num
    if non_present_sum % 2:
        return bin(non_present_sum)[2:]
    else:
        return hex(non_present_sum)[2:].upper()