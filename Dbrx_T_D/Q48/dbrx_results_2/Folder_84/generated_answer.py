def return_binary_or_hexa(indices_tuple):
    a = indices_tuple[32]
    b = indices_tuple[44]
    sum = 0
    present_numbers = set(indices_tuple[32:45])
    for num in range(a + 1, b):
        if num not in present_numbers:
            sum += num
    if sum % 2 != 0:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()