def return_binary_or_hexa(int_tuple):
    a = int_tuple[11]
    b = int_tuple[76]
    total = 0
    for num in range(a + 1, b):
        if num not in int_tuple:
            total += num
    if total % 2 == 0:
        return hex(total)[2:]
    else:
        return bin(total)[2:]