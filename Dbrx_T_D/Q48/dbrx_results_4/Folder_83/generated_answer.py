def return_binary_or_hexa(input_tuple):
    a = input_tuple[90]
    b = input_tuple[200]
    non_present_sum = sum((i for i in range(a + 1, b) if i not in input_tuple[90:201]))
    if non_present_sum % 2:
        return bin(non_present_sum)[2:]
    else:
        return hex(non_present_sum)[2:].upper()