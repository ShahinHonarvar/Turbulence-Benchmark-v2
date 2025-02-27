def return_binary_or_hexa(int_tuple):
    a = int_tuple[49]
    b = int_tuple[74]
    mask = 0
    for num in int_tuple[49:75]:
        mask |= num
    sum = a + b + 1 & ~mask
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()