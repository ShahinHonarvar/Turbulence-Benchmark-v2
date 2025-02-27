def return_binary_or_hexa(input_tuple):
    a = input_tuple[3]
    b = input_tuple[8]
    present_numbers = set(input_tuple[3:9])
    total = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:].upper()