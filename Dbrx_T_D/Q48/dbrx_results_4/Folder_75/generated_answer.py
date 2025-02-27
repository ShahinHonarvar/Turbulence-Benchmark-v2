def return_binary_or_hexa(int_tuple):
    a = int_tuple[20]
    b = int_tuple[51]
    non_present_sum = 0
    for num in range(a + 1, b):
        if num not in int_tuple[20:52]:
            non_present_sum += num
    if non_present_sum % 2 == 1:
        return bin(non_present_sum)[2:]
    else:
        return hex(non_present_sum)[2:].upper()